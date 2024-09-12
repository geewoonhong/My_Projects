from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView, #generic view that displays form for creating an object
    UpdateView, #generic view that displays form for editing an existing obj 
    DeleteView, #display confirmation page and deletes object
)
from .models import ToDoList, ToDoItem

# Create your views here.
class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView): #extends generic Django class ListView
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self): #overide original get method with a filtered one 
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self): #set up context dictionary which is used to populate html template with values
        #super is used to not lose default context data set up by parent class 
        # avoid the need to rewrite a setup for context dictionary
        context = super().get_context_data()

        #add a new key-value pair to context dictionary key is "todo_list" value is the object retrieved
        #by the get method 
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"]) #keyword arg list_id
        return context #this value will be passed to the template


#logic to create new lists
class ListCreate(CreateView):
    model = ToDoList
    #fields that should be presented to user
    fields = ["title"]
    template_name = "todo_app/todolist_form.html"
    success_url = reverse_lazy('index')  #on a success we need to give a url to redirect to

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context


#logic to create new item for a list
class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])


#logic to update an item from a list
class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

#list delete
class ListDelete(DeleteView):
    model = ToDoList
    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem
    
    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        content["todo_list"] = self.object.todo_list
        return context
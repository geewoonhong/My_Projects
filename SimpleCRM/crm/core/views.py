from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy, path
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contact, Task, Opportunity, Interaction
from .forms import CustomUserCreationForm

# Create your views here.
# View for the login page
class CrmLoginView(LoginView):
	template_name = 'registration/login.html'


# View for new user registration
def register(request):
	if request.method=='POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return (redirect('index'))
	else:
		form = CustomUserCreationForm()
	return render(request, 'registration/register.html', {'form': form})

# View for landing page
def index(request):
	total_contacts = Contact.objects.count()
	total_tasks = Task.objects.count()
	total_opportunities = Opportunity.objects.count()
	total_interactions = Interaction.objects.count()

	context = {
		'total_contacts': total_contacts,
		'total_tasks': total_tasks,
		'total_opportunities': total_opportunities,
		'total_interactions': total_interactions,
	}
	return render(request, 'core/index.html', context)



### CRUD for Contacts ###
# Create Contacts
class ContactCreateView(CreateView):
	model = Contact
	template_name = 'core/contact_form.html'
	fields = ['first_name', 'last_name', 'email', 'company', 'position']
	success_url = reverse_lazy('contact-list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

# Read (List) Contacts
class ContactListView(ListView):
	model = Contact
	template_name = 'core/contact_list.html'
	context_object_name = 'contacts'

# Update Contacts
class ContactUpdateView(UpdateView):
	model = Contact
	template_name = 'core/contact_form.html'
	fields = ['first_name', 'last_name', 'email', 'company', 'position']
	success_url = reverse_lazy('contact-list')

	def get_queryset(self):
		queryset = super().get_queryset() #get all the contacts for now
		if not self.request.user.is_superuser: #if not the superuser filter the contacts
			queryset = queryset.filter(user=self.request.user)
		return queryset

	def dispatch(self, request, *args, **kwargs): #method intercepts request to view before main logic
		contact = self.get_object()
		if contact.user != request.user and not request.user.is_superuser:
			raise PermissionDenied("You are not allowed to edit this contact.")
		return super().dispatch(request, *args, **kwargs) #if permission check passes, proceed with normal view

# Delete Contact
class ContactDeleteView(DeleteView):
	model = Contact
	template_name = 'core/contact_confirm_delete.html'
	success_url = reverse_lazy('contact-list')

	def dispatch(self, request, *args, **kwargs):
		contact = self.get_object()
		if contact.user != request.user and not request.user.is_superuser:
			raise PermissionDenied("You are not allowed to delete this contact.")
		return super().dispatch(request, *args, **kwargs)

#Contact Detail View
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'core/contact_detail.html', {'contact': contact})





### CRUD for Tasks ###
# Create Tasks
class TaskCreateView(CreateView):
	model = Task
	template_name = 'core/task_form.html'
	fields = ['title', 'description', 'contact', 'due_date', 'status']
	success_url = reverse_lazy('task-list')

# Read (List) Tasks
class TaskListView(ListView):
	model = Task
	template_name = 'core/task_list.html'
	context_object_name = 'tasks'

# Update Task
class TaskUpdateView(UpdateView):
	model = Task
	template_name = 'core/task_form.html'
	fields = ['title', 'description', 'contact', 'due_date', 'status']
	success_url = reverse_lazy('task-list')

# Delete Task
class TaskDeleteView(DeleteView):
	model = Task
	template_name = 'core/task_confirm_delete.html'
	success_url = reverse_lazy('task-list')




### CRUD for Opportunities ###
# Create Opportunities
class OpportunityCreateView(CreateView):
	model = Opportunity
	template_name = 'core/opportunity_form.html'
	fields = ['name', 'contact', 'value', 'stage']
	success_url = reverse_lazy('opportunity-list')

# Read (list) Opportunities
class OpportunityListView(ListView):
	model = Opportunity
	template_name = 'core/opportunity_list.html'
	context_object_name = 'opportunities'

# Update Opportunities
class OpportunityUpdateView(UpdateView):
	model = Opportunity
	template_name = 'core/opportunity_form.html'
	fields = ['name', 'contact', 'value', 'stage']
	success_url = reverse_lazy('opportunity-list')

# Delete Opportunities
class OpportunityDeleteView(DeleteView):
	model = Opportunity
	template_name = 'core/opportunity_confirm_delete.html'
	success_url = reverse_lazy('opportunity-list')




### CRUD for Interaction ###
# Create Interaction
class InteractionCreateView(CreateView):
	model = Interaction
	template_name = 'core/interaction_form.html'
	fields = ['interaction_type', 'contact', 'date', 'notes']
	success_url = reverse_lazy('interaction-list')

# Read (list) Interactions
class InteractionListView(ListView):
	model = Interaction
	template_name = 'core/interaction_list.html'
	context_object_name = 'interactions'

# Update Interactions
class InteractionUpdateView(UpdateView):
	model = Interaction
	template_name = 'core/interaction_form.html'
	fields = ['interaction_type', 'contact', 'date', 'notes']
	success_url = reverse_lazy('interaction-list')

# Delete Interactions
class InteractionDeleteView(DeleteView):
	model = Interaction
	template_name = 'core/interaction_confirm_delete.html'
	success_url = reverse_lazy('interaction-list')

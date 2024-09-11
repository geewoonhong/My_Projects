from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absoulte_url(self):
        return reverse("list", args=[self.id])
    
    #provide human-readable rep of model instance
    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE) #link item to list many-to-one

    #syntax of reverse :used to make URLS from patterns by name
    #reverse(name of URL pattern, args to be included in URL)
    def get_absoulte_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = [
            "due_date"
        ]
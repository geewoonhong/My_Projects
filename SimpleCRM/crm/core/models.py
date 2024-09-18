from django.db import models

# Create your models here.
# models for databases: contacts, tasks, opportunities, interactions

class contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	company = models.CharField(max_length=100, blank=True, null=True)
	position = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class task(models.model):
	STATUS = [
		('pending', 'Pending'),
		('completed', 'Completed'),
	]

	title = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	due_date = models.DateTimeField()
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='tasks')
	status = models.CharField(max_length=20, choices=STATUS, default='pending')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

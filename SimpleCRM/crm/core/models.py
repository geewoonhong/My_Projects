from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models for databases: contacts, tasks, opportunities, interactions

class Contact(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	company = models.CharField(max_length=100, blank=True, null=True)
	position = models.CharField(max_length=100, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"



class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
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



class Opportunity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	STAGE_CHOICES = [
		('new', 'New'),
		('in_progress', 'In Progress'),
		('won', 'Won'),
		('lost', 'Lost'),
	]

	name = models.CharField(max_length=200)
	value = models.DecimalField(max_digits=10, decimal_places=2)
	stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='new')
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='opportunities')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Interaction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	TYPE_CHOICES = [
		('email', 'Email'),
		('call', 'Call'),
		('meeting', 'Meeting'),
	]

	interaction_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='interactions')
	date = models.DateTimeField()
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return f"{self.interaction_type} with {self.contact} on {self.date}"

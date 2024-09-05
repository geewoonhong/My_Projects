from django.db import models

# Create your models here.
# with an ORM, models are classes you build to represent database tables
class Category(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = "categories"

	#add following method to model classes to give str representation
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField("Category", related_name="posts")

	def __str__(self):
		return self.title

class Comment(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	#conenct many comments to one post
	# (relate to post, delete if post is gone)
	post = models.ForeignKey("Post", on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.author} on '{self.post}'"

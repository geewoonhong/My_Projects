from django.contrib import admin
from blog.models import Category, Comment, Post

# Register your models here.

#can add attributes or methods later on to customize what
#admin page shows
class CategoryAdmin(admin.ModelAdmin):
	pass

class PostAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass

#register to show on the localhost
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

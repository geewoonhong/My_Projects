from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('contacts/', views.ContactListView.as_view(), name='contact-list'),
	path('contacts/create/', views.ContactCreateView.as_view(), name='contact-create'),
	path('contacts/update/<int:contact_id>/', views.ContactUpdateView.as_view(), name='contact-update'),
	path('contacts/delete/<int:contact_id>/', views.ContactDeleteView.as_view(), name='contact-delete'),
	path('contacts/<int:contact_id>/', views.contact_detail, name='contact-detail'),
	path('tasks/', views.TaskListView.as_view(), name='task-list'),
	path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
	path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
	path('tasks/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
	path('opportunities/', views.OpportunityListView.as_view(), name='opportunity-list'),
	path('opportunities/create/', views.OpportunityCreateView.as_view(), name='opportunity-create'),
	path('opportunities/update/<int:pk>/', views.OpportunityUpdateView.as_view(), name='opportunity-update'),
	path('opportunities/delete/<int:pk>/', views.OpportunityDeleteView.as_view(), name='opportunity-delete'),
	path('interactions/', views.InteractionListView.as_view(), name='interaction-list'),
	path('interactions/create/', views.InteractionCreateView.as_view(), name='interaction-create'),
	path('interactions/update/<int:pk>/', views.InteractionUpdateView.as_view(), name='interaction-update'),
	path('interactions/delete/<int:pk>/', views.InteractionDeleteView.as_view(), name='interaction-delete'),
]

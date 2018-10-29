from django.urls import path, include
from .import views

urlpatterns = [
	path('', views.home, name='home'),
	path('list', views.doc_list, name='doc_list'),
	path('section/<int:pk>/', views.doc_detail, name='doc_detail'),
	path('section/new', views.doc_new, name='doc_new'),
	path('section/<int:pk>/edit/', views.doc_edit, name='doc_edit'),
]
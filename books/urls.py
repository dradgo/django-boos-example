from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.manage_book, name='add_book'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.manage_category, name='add_category'),
    path('category/edit/<int:pk>/', views.manage_category, name='edit_category'),
    path('category/delete/<int:pk>/', views.delete_category, name='delete_category'),
    path('edit/<int:pk>/', views.manage_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
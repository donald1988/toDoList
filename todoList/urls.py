from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listItems),
    path('insert_todo/', views.insert, name = 'insert_items'),
    path('delete_todo/<int:todo_id>/', views.delete, name = 'delete_items')
]
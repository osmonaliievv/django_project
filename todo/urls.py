from django.urls import path
from . import views

urlpatterns = [
    path('create_todo/', views.create_todo_view, name='create_todo'),
    path('todo_list/', views.todo_list_view, name='todo_list'),
    path('todo_list/<int:id>/', views.todo_detail_view, name='todo_detail'),
    path('todo_list/<int:id>/update/', views.todo_update_view, name='todo_update'),
    path('todo_list/<int:id>/delete/', views.delete_todo_view, name='todo_delete'),
]

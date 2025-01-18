from django.urls import path
from . import views

urlpatterns = [
    path('create_todo/', views.CreateTodoView.as_view(), name='create_todo'),
    path('todo_list/', views.TodoListView.as_view(), name='todo_list'),
    path('todo_list/<int:id>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo_list/<int:id>/update/', views.UpdateTodoView.as_view(), name='todo_update'),
    path('todo_list/<int:id>/delete/', views.DeleteTodoView.as_view(), name='todo_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
    path('current_time/', views.current_time, name='current_time'),
    path('search/', views.SearchView.as_view(), name='search'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('mybook_list', views.LibrusecListView.as_view(), name='mybook_list'),
    path('mybook_form', views.LibrusecFormView.as_view(), name='mybook_form'),
]

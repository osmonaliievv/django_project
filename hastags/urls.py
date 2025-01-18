from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.AllProductsView.as_view(), name='all_products'),
    path('drama/', views.DramaView.as_view(), name='drama'),
    path('fairy_tale/', views.FairyTaleView.as_view(), name='fairy_tale'),
    path('fantasy/', views.FantasyView.as_view(), name='fantasy'),
]

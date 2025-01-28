from django.urls import path
from . import views

urlpatterns = [
    path('create_recipe/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('create_ingredient/', views.CreateIngredientView.as_view(), name='create_ingredient'),
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:id>/delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm


class CreateRecipeView(generic.CreateView):
    template_name = 'recipe/create_recipe.html'
    form_class = RecipeForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        return super(CreateRecipeView, self).form_valid(form=form)


class CreateIngredientView(generic.CreateView):
    template_name = 'recipe/create_ingredient.html'
    form_class = IngredientForm
    success_url = '/recipe_list/'

    def form_valid(self, form):
        return super(CreateIngredientView, self).form_valid(form=form)


class RecipeListView(generic.ListView):
    template_name = 'recipe/recipe_list.html'
    context_object_name = 'recipes'
    model = Recipe

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class RecipeDetailView(generic.DetailView):
    template_name = 'recipe/recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(Recipe, id=recipe_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.all()
        return context


class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipe/confirm_delete.html'
    success_url = '/recipe_list/'

    def get_object(self, **kwargs):
        recipe_id = self.kwargs.get('id')
        return get_object_or_404(Recipe, id=recipe_id)

from django.shortcuts import render, get_object_or_404
from .models import Recipe


def recipe_list(request):
    ctx = {"recipes": Recipe.objects.all()}
    return render(request, "recipes/recipe_list.html", ctx)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ctx = {
        "recipe": recipe,
    }
    return render(request, "recipes/recipe.html", ctx)

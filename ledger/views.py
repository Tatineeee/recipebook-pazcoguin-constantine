from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required


def recipe_list(request):
    ctx = {"recipes": Recipe.objects.all()}
    return render(request, "recipes/recipe_list.html", ctx)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "recipes/recipe.html", ctx)

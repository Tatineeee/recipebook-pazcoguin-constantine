from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage


def recipe_list(request):
    ctx = {"recipes": Recipe.objects.all()}
    return render(request, "recipes/recipe_list.html", ctx)


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "recipes/recipe.html", ctx)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["name", "author"]
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("recipe_list")


class RecipeImageUploadView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ["image", "description"]
    template_name = "recipes/recipe_image_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.kwargs["pk"]})

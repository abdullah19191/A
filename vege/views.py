from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def recipes(request):

    if request.method == "POST":
        data = request.POST
        recipe_names = data.get("recipe_name")
        recipe_image = request.FILES.get("recipe_image")
        recipe_discriptions = data.get("recipe_discription")

        Recipe.objects.create(
            recipe_name=recipe_names,
            recipe_image=recipe_image,
            recipe_discription=recipe_discriptions,
        )

        return redirect("/recipes")

    queryset = Recipe.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get("search"))
    context = {"recipes": queryset}
    return render(request, "recipes.html", context)


def update_recipe(request, id):

    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_names = data.get("recipe_name")
        recipe_image = request.FILES.get("recipe_image")
        recipe_discriptions = data.get("recipe_discription")

        queryset.recipe_name = recipe_names
        queryset.recipe_discription = recipe_discriptions
        queryset.save()
        return redirect("/recipes")

    context = {"recipe": queryset}
    return render(request, "update_recipes.html", context)


def delete_recipe(request, id):

    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/recipes")


def login_page(request):
    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Account Already Exist.")
            return redirect("/register/")
        user = User.objects.create(
            first_name=first_name,
            username=username,
            password=password,
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully.")
        return redirect("/register/")

    return render(request, "register.html")

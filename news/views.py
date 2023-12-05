from news.models import Category, News
from news.forms import CategoriesForms
from django.shortcuts import redirect, render


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    context = {"new": News.objects.get(id=id)}
    return render(request, "news_details.html", context)


def categories_form(request):
    context = {"form": CategoriesForms()}

    if request.method == "POST":
        name_tag = request.POST.get("name")
        Category.objects.create(name=name_tag)
        return redirect("home-page")
    return render(request, "categories_form.html", context)

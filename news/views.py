from news.models import Category, News
from news.forms import CategoriesForms
from django.shortcuts import redirect, render, get_object_or_404


def home(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, "home.html", context)


def news_details(request, id):
    obj_news = get_object_or_404(News, id=id)
    context = {
        "new": obj_news, 
        "categories": obj_news.categories.all()
    }
    return render(request, "news_details.html", context)


def categories_form(request):
    if request.method == "POST":
        Category.objects.create(name=request.POST.get("name"))
        return redirect("home-page")

    context = {
        "form": CategoriesForms()
    }
    return render(request, "categories_form.html", context)

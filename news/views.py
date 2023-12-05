from news.models import Category, News
from news.forms import CategoriesForms
from django.shortcuts import redirect, render, get_object_or_404


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    obj_news = get_object_or_404(News, id=id)
    all_categories = obj_news.categories.all()
    context = {"new": obj_news, "categories": all_categories}
    return render(request, "news_details.html", context)


def categories_form(request):
    context = {"form": CategoriesForms()}

    if request.method == "POST":
        name_tag = request.POST.get("name")
        Category.objects.create(name=name_tag)
        return redirect("home-page")
    return render(request, "categories_form.html", context)

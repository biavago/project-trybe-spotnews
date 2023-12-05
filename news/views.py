from news.models import News
from django.shortcuts import render


def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)

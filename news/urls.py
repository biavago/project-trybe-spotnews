from news.views import categories_form, home, news_details
from django.urls import path


urlpatterns = [
    path("", home, name="home-page"),
    path("categories", categories_form, name="categories-form"),
    path("news/<int:new_id>", news_details, name="news-details-page"),
]

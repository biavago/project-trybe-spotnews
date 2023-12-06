from news.models import News
from news_rest.serializers.news_serializer import NewsSerializer
from rest_framework import viewsets


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

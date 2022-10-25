from django.urls import path, include
from crawler.views import CrawlerAPI

urlpatterns = [
    path('', CrawlerAPI.as_view())
]

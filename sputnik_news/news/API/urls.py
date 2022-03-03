
from django.urls import path
from news.API.views import  NewsDetailView,NewsDetailPage

urlpatterns = [

    path('news',NewsDetailView.as_view()),
    path('news/<int:pk>',NewsDetailPage.as_view())
]
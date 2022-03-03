from rest_framework.generics import ListAPIView,RetrieveAPIView
from news.models import NewsDetail
from news.API.serializers import NewsDetailSerializer

class NewsDetailView(ListAPIView):
    queryset=NewsDetail.objects.all()
    serializer_class=NewsDetailSerializer


class NewsDetailPage(RetrieveAPIView):
    queryset=NewsDetail.objects.all()
    serializer_class=NewsDetailSerializer




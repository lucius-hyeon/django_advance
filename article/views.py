from rest_framework.response import Response
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleSerializer
from django.contrib.auth.models import AbstractUser

class ArticleView(APIView):
    def get(self, request, format=None):
        article  = Article.objects.all()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

# Create your views here.

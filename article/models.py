from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user' )
    title = models.CharField(max_length = 100, null=True, blank =True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    

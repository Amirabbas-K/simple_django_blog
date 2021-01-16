from django.db import models

# Create your models here.
class Posts (models.Model):
    thumbnail = models.ImageField(upload_to = 'static/img/')
    title = models.CharField(max_length=120)
    body = models.CharField(max_length=800)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=12)
from django.shortcuts import render
from rest_framework.decorators import api_view
from Blog.models import Posts
from .serializer import post_serializer
from rest_framework.response import Response
# Create your views here.
@api_view(["GET" , "POST"])
def collect_post (request): # collect and send posts 
    posts =  Posts.objects.all()
    serializer =  post_serializer(posts , many = True)
    return Response(serializer.data)


from django.shortcuts import render
from rest_framework.decorators import api_view
from Blog.models import Posts
from .serializer import post_serializer
from django.http import HttpResponse
from rest_framework.response import Response
# Create your views here.
@api_view(["GET" , "POST"])
def collect_post (request): # collect and send posts # Get all posts
    posts =  Posts.objects.all()
    serializer =  post_serializer(posts , many = True)
    return Response(serializer.data)

@api_view(["GET"])
def post_finder (request , id ): # find a special post
    try:
        post = Posts.objects.get(id =id)
    except Posts.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = post_serializer(post)
        return Response(serializer.data)
@api_view(["PUT"])
def update_post(request , id ):
    try:
        post = Posts.objects.get (id = id )
    except post.DoesNotExist :
        return HttpResponse(status=404)

    if request.method == "PUT":
        serializer = post_serializer(post , data=request.data )
        if serializer.is_valid() :
            serializer.save()
            return Response(data=request.data)
        return HttpResponse(status = 400 )


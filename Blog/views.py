from django.shortcuts import render , redirect
from .forms import Post_frm
from .models import Posts
# Create your views here.
def add_post (request):
    model_frm = Post_frm()
    if request.method == "POST":
        model_frm = Post_frm(request.POST , request.FILES)
        if model_frm.is_valid():
            model_frm.save()
    data = {"form" : model_frm}
    return render(request , "./post/add.html" , data)
def edit_post (request , id):
    get_db = Posts.objects.get(id = id)
    data = {"post":get_db}
    if request.method == "POST":
        author = request.POST['author']
        body = request.POST['body']
        tag = request.POST['tag']
        title = request.POST['title']
        model = Posts.objects.filter(id=id).update(tag=tag, body=body, author=author , title=title)
    return render (request , "./post/edit.html" , data)
def delete_post (request , id):
    if request.method == "POST":
        get_db = Posts.objects.get(id = id).delete()
        return redirect ("main_page_url")
    data = {}
    return render(request , "./post/delete.html" )
def main_page (request):
    get_db = Posts.objects.all()
    data = {"posts" : get_db}
    return render(request , "main_page.html" , data)
def read_more (request , id):
    the_post = Posts.objects.get(id=id)
    # view counter
    the_post.view_count=the_post.view_count+1
    the_post.save()
    data = {'post': the_post}
    return render(request, './post/read_more.html', data)

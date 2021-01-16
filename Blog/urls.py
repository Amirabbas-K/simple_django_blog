from django.urls import path
from .views import add_post , edit_post , delete_post , main_page , read_more
urlpatterns = [
    path('add_post' ,add_post , name = "add_posts_url" ),
    path('edit_post/<int:id>' , edit_post , name = "edit_post_url") ,
    path('delete_post/<int:id>' , delete_post , name = "delete_post_url") ,
    path('' , main_page , name = "main_page_url"),
    path('read_more/<int:id>' , read_more , name="read_more_url")
]
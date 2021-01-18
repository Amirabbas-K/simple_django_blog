from django.urls import path
from .views import collect_post
urlpatterns = [
        path('collect_post/' , collect_post , name = "get_post_api_url" )
]

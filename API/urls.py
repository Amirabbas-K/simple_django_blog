from django.urls import path
from .views import collect_post , post_finder
urlpatterns = [
        path('collect_post/' , collect_post , name = "get_post_api_url" ),
        path('get_post/<int:id>' , post_finder , name = "open_post_api_url" )
]

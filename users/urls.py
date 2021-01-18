from django.urls import path , include
from .views import sign_up
urlpatterns = [
    path('sign_up/' , sign_up , name = "sign_up_urls" ),
    path('' , include('django.contrib.auth.urls')  ,name = "login" )
    ]

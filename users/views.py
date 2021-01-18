from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid :
            form.save()
    data = {"form" : form }
    return render (request , "registration/sign_up.html" , data)


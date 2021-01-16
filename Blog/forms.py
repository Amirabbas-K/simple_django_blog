from django.forms import ModelForm
from .models import Posts

class Post_frm(ModelForm):
    class Meta():
        model = Posts
        # fields = "__all__"
        fields = ['title' , 'body' , 'author' , 'tag' ]

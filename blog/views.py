from django.shortcuts import render
from blog.models import Post
# Create your views here.

def blog(request):
    post = Post.objects.all()
    data = {
        'pots' : post
    }
    return(render(request, "mascotitas/home.html", data))





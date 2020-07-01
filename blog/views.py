from django.shortcuts import render
from .models import Blog

def blogPage(request):
    blogs = Blog.objects
    return render(request,'blog/blogHome.html',{ 'blogs': blogs})

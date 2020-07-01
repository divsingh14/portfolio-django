from django.shortcuts import render,get_object_or_404
from .models import Blog

def blogPage(request):
    blogs = Blog.objects
    return render(request,'blog/blogHome.html',{ 'blogs': blogs})

def detailBlog(request,blogId):
    detailBlog = get_object_or_404(Blog,pk=blogId)
    return render(request,'blog/blogDetail.html',{ 'blog' : detailBlog})
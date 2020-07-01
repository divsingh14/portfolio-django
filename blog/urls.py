from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogPage,name='blogPage'),
    path('<int:blogId>/',views.detailBlog , name='blogDetails')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('single_post', views.single_post, name='single_post'),
    path('contact', views.contact, name='contact'),
    path('category', views.category, name='category'),
    path('starter_page', views.starter_page, name='starter_page'),
    path('blog_details/<id>', views.blog_details, name='blog_details'),
    path('comments', views.comments, name='comments')
]
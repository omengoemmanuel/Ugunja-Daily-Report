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
    path('comments', views.comments, name='comments'),
    path('detail_col1/<id>', views.detail_col1, name='detail_col1'),
    path('comment_col11', views.comment_col11, name='comment_col11'),
    path('detail_col2/<id>', views.detail_col2, name='detail_col2'),
    path('comment_col22', views.comment_col22, name='comment_col22'),
    path('detail_col3/<id>', views.detail_col3, name='detail_col3'),
    path('comment_col33', views.comment_col33, name='comment_col33'),

    # Culture Section
    path('main_culture/<id>', views.main_culture, name='main_culture'),
    path('cul_col2/<id>', views.cul_col2, name='cul_col2'),
    path('cul_col1/<id>', views.cul_col1, name='cul_col1'),
    path('comm_cul_col1', views.comm_cul_col1, name='comm_cul_col1'),
    path('cul_col22/<id>', views.cul_col22, name='cul_col22'),
]
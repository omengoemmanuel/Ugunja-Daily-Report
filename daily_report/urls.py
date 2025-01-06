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
    path('cul_col3/<id>', views.cul_col3, name='cul_col3'),
    path('comm_cul_col3', views.comm_cul_col3, name='comm_cul_col3'),

    # Business Section
    path('bus_col1/<id>', views.bus_col1, name='bus_col1'),
    path('comm_bus_col1', views.comm_bus_col1, name='comm_bus_col1'),
    path('busines_main/<id>', views.busines_main, name='busines_main'),
    path('bus_sub_trend/<id>', views.bus_sub_trend, name='bus_sub_trend'),
    path('business_col21/<id>', views.business_col21, name='business_col21'),
    path('comm_bus_col21', views.comm_bus_col21, name='comm_bus_col21'),


    # lifestyle
    path('main_lifestyle/<id>', views.main_lifestyle, name='main_lifestyle'),
    path('life_col1/<id>', views.life_col1, name='life_col1'),
    path('comment_col1', views.comment_col1, name='comment_col1'),


    # New messages
    path('new_message', views.new_message, name='new_message'),
]
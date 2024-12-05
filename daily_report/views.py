from django.shortcuts import render, redirect
from .models import sliders, main_trending_headline, comment, sub_trending_col_1
from django.contrib import messages


# Create your views here.
def index(request):
    slide = sliders.objects.all()
    trend = main_trending_headline.objects.all()
    sub_trend_1 = sub_trending_col_1.objects.all()
    return render(request, 'index.html', {'slide': slide, 'trend': trend, 'sub_trend_1': sub_trend_1})


def about(request):
    return render(request, 'about.html')


def single_post(request):
    return render(request, 'single-post.html')


def contact(request):
    return render(request, 'contact.html')


def category(request):
    return render(request, 'category.html')


def starter_page(request):
    return render(request, 'starter-page.html')


def blog_details(request, id):
    trends = main_trending_headline.objects.all()
    return render(request, 'blog_details.html', {'trends': trends})


def comments(request):
    if request.method == 'POST':
        comm = request.POST.get('comm')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        commen = comment(comm=comm, full_name=full_name, email=email, phone=phone)
        commen.save()
        messages.success(request, "Comment uploaded successfully")
        return redirect('index')

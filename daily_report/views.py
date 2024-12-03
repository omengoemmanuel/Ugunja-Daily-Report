from django.shortcuts import render
from .models import sliders


# Create your views here.
def index(request):
    slide = sliders.objects.all()
    return render(request, 'index.html', {'slide': slide})


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

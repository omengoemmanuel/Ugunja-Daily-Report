from django.shortcuts import render, redirect
from .models import sliders, main_trending_headline, comment, sub_trending_col_1, sub_trending_col_2, \
    sub_trending_col_3, comment_col1, comment_col2, comment_col3, culture_main, culture_main_support
from django.contrib import messages


# Create your views here.
def index(request):
    slide = sliders.objects.all()
    trend = main_trending_headline.objects.all()
    sub_trend_1 = sub_trending_col_1.objects.all()
    sub_trend_2 = sub_trending_col_2.objects.all()
    sub_trend_3 = sub_trending_col_3.objects.all()
    Culture_main = culture_main.objects.all()
    return render(request, 'index.html',
                  {'slide': slide, 'trend': trend, 'sub_trend_1': sub_trend_1, 'sub_trend_2': sub_trend_2,
                   'sub_trend_3': sub_trend_3, 'Culture_main': Culture_main})


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


def detail_col1(request, id):
    det_col1 = sub_trending_col_1.objects.get(id=id)
    comment1 = comment_col1.objects.all()
    return render(request, 'detail_col1.html', {'det_col1': det_col1, 'comment1': comment1})


def comment_col11(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment1 = comment_col1(comment=comment, full_name=full_name, email=email, phone=phone)
        comment1.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')


def detail_col2(request, id):
    det_col2 = sub_trending_col_2.objects.get(id=id)
    comment2 = comment_col2.objects.all()
    return render(request, 'detail_col2.html', {'det_col2': det_col2, 'comment2': comment2})


def comment_col22(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment2 = comment_col2(comment=comment, full_name=full_name, email=email, phone=phone)
        comment2.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')


def detail_col3(request, id):
    det_col3 = sub_trending_col_3.objects.get(id=id)
    comment3 = comment_col3.objects.all()
    return render(request, 'detail_col3.html', {'det_col3': det_col3, 'comment3': comment3})


def comment_col33(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment3 = comment_col3(comment=comment, full_name=full_name, email=email, phone=phone)
        comment3.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')

# culture section
def main_culture(request, id):
    cul = culture_main.objects.get(id=id)
    supp = culture_main_support.objects.all()
    return render(request, 'culture/main.html',{'cul': cul, 'supp': supp})
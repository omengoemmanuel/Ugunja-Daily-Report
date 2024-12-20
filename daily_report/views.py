from django.shortcuts import render, redirect
from .models import sliders, main_trending_headline, comment, sub_trending_col_1, sub_trending_col_2, \
    sub_trending_col_3, comment_col1, comment_col2, comment_col3, culture_main, culture_main_support, culture_col11, \
    culture_col12, comment_cul_col1, culture_col2, culture_col3, comment_cul_col3, business_col1, comment_bus_col1, \
    business_main, business_main_support, business_sub_trending, business_post_1, comment_bus_col21
from django.contrib import messages


# Create your views here.
def index(request):
    slide = sliders.objects.all()
    trend = main_trending_headline.objects.all()
    sub_trend_1 = sub_trending_col_1.objects.all()
    sub_trend_2 = sub_trending_col_2.objects.all()
    sub_trend_3 = sub_trending_col_3.objects.all()
    Culture_main = culture_main.objects.all()
    culture_col1 = culture_col11.objects.all()
    culturecol2 = culture_col12.objects.all()
    cul_col_2 = culture_col2.objects.all()
    cul_col_3 = culture_col3.objects.all()
    busi_col1 = business_col1.objects.all()
    Business_main = business_main.objects.all()
    bus_sub_trending = business_sub_trending.objects.all()
    bus_post_1 = business_post_1.objects.all()
    return render(request, 'index.html',
                  {'slide': slide, 'trend': trend, 'sub_trend_1': sub_trend_1, 'sub_trend_2': sub_trend_2,
                   'sub_trend_3': sub_trend_3, 'Culture_main': Culture_main, 'culture_col1': culture_col1,
                   'culturecol2': culturecol2, 'cul_col_2': cul_col_2, 'cul_col_3': cul_col_3,
                   'busi_col1': busi_col1, 'Business_main': Business_main, 'bus_sub_trending': bus_sub_trending, 'bus_post_1': bus_post_1})


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
    return render(request, 'culture/main.html', {'cul': cul, 'supp': supp})


def cul_col2(request, id):
    cult_col12 = culture_col12.objects.get(id=id)
    return render(request, 'culture/cul_col.html', {'cult_col12': cult_col12})


def cul_col1(request, id):
    cul_11 = culture_col11.objects.get(id=id)
    cul_comm = comment_cul_col1.objects.all()
    return render(request, 'culture/cul_col1.html', {'cul_11': cul_11, 'cul_comm': cul_comm})


def comm_cul_col1(request):
    if request.method == 'POST':
        comm = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment2 = comment_cul_col1(comm=comm, full_name=full_name, email=email, phone=phone)
        comment2.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')


def cul_col22(request, id):
    cul_22 = culture_col2.objects.get(id=id)
    return render(request, 'culture/cul_col2.html', {'cul_22': cul_22})


def cul_col3(request, id):
    cul_3 = culture_col3.objects.get(id=id)
    comment_cul3 = comment_cul_col3.objects.all()
    return render(request, 'culture/cul_col3.html', {'cul_3': cul_3, 'comment_cul3': comment_cul3})


def comm_cul_col3(request):
    if request.method == 'POST':
        comm = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment3 = comment_cul_col3(comm=comm, full_name=full_name, email=email, phone=phone)
        comment3.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')


# Business section
def bus_col1(request, id):
    buss_col1 = business_col1.objects.get(id=id)
    buss_col1_comm = comment_bus_col1.objects.all()
    return render(request, 'business/bus_col1.html', {'buss_col1': buss_col1, 'buss_col1_comm': buss_col1_comm})


def comm_bus_col1(request):
    if request.method == 'POST':
        comm = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment4 = comment_bus_col1(comm=comm, full_name=full_name, email=email, phone=phone)
        comment4.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')


def busines_main(request, id):
    business_ma = business_main.objects.get(id=id)
    support_main_bus = business_main_support.objects.all()
    return render(request, 'business/main.html', {'business_ma': business_ma, 'support_main_bus': support_main_bus})


def bus_sub_trend(request, id):
    sub_trends = business_sub_trending.objects.get(id=id)
    return render(request, 'business/sub_trending.html', {'sub_trends': sub_trends})

def business_col21(request, id):
    bus_col21 = business_post_1.objects.get(id=id)
    com_bus = comment_bus_col21.objects.all()
    return render(request, 'business/business_col21.html', {'bus_col21': bus_col21, 'com_bus': com_bus})

def comm_bus_col21(request):
    if request.method == 'POST':
        comm = request.POST.get('comment')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        comment5 = comment_bus_col21(comm=comm, full_name=full_name, email=email, phone=phone)
        comment5.save()
        messages.success(request, "Comment uploaded successfully")

        return redirect('index')
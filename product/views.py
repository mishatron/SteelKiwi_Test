import datetime
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.shortcuts import render

# Create your views here.
from product.models import Category, Product


def index(request):
    cat_list = Category.objects.all()
    message = ''
    if cat_list.count() == 0:
        global message
        message = 'No categories'
    return render(request, 'products.html', {'cat_list': cat_list, 'message': message})


def products(request):
    cat_list = Category.objects.all()
    message = ''
    if cat_list.count() == 0:
        global message
        message = 'No categories'
    return render(request, 'products.html', {'cat_list': cat_list, 'message': message})


def products_category(request,category_slug):
    cat = Category.objects.get(slug=category_slug)
    cat_info_list = Product.objects.filter(category=cat.id)
    return render(request, 'category_products.html', {'cat_info_list': cat_info_list, 'category': category_slug})


def products24(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    created_products = Product.objects.filter(
         created_at__gte=date_from)
    message = ''
    if created_products.count() == 0:
        global message
        message = 'No products'
    return render(request, 'products24.html', {'list24': created_products, 'message': message})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def login_view(request):
    un = request.POST['_user']
    pas = request.POST['_pass']
    user = authenticate(username=un, password=pas)
    login(request, user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def register_view(request):
    return render(request, 'registration.html')


def register_user(request):
    un = request.POST['_user']
    email = request.POST['_email']
    fn = request.POST['_firstName']
    ln = request.POST['_lastName']
    pas = request.POST['_pass']
    pas2 = request.POST['_pass2']

    if pas == pas2:
        user = User.objects.create_user(un, email, pas)
        user.first_name = fn
        user.last_name = ln
        user.save()
    user = authenticate(username=un, password=pas)
    login(request, user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def product_info(request, category_slug, product_slug):
    prod = Product.objects.get(slug=product_slug)
    return render(request, 'product_info.html', {'prod': prod})


def product_info2(request, product_slug):
    prod = Product.objects.get(slug=product_slug)
    return render(request, 'product_info.html', {'prod': prod})

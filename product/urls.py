"""SteelKiwi2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'^logout/$',  views.logout_view),
    url(r'^login/$',  views.login_view),
    url(r'^register/$', views.register_view),
    url(r'^register/register_user/$', views.register_user),
    url(r'^$', views.index, name='index'),
    url(r'^products/$', views.products, name='products'),
    url(r'^product/(?P<category_slug>[-\w]+)/$', views.products_category, name='products_category'),
    url(r'^product/(?P<category_slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', views.product_info, name='product_info'),
    url(r'^product_info/(?P<product_slug>[-\w]+)/$', views.product_info2, name='product_info2'),
    url(r'^products24/$', views.products24, name='products24'),
]

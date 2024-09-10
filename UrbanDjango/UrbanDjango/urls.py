"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task4 import views as task4_views
from task5 import views as task5_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('platform/', task4_views.platform, name='platform'),
    path('platform/games/', task4_views.games, name='games'),
    path('platform/cart/', task4_views.cart, name='cart'),
    path('', task5_views.sign_up_by_html, name='html_signup'),
    path('django_sign_up/', task5_views.sign_up_by_django, name='django_signup'),
]
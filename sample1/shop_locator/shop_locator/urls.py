"""
URL configuration for shop_locator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from shops import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shop_list, name='shop_list'),
    path('shop/<int:pk>/', views.shop_detail, name='shop_detail'),
    path('shop/new/', views.shop_create, name='shop_create'),
    path('shop/<int:pk>/edit/', views.shop_update, name='shop_update'),
]
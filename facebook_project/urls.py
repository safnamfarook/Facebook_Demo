"""facebook_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('fb_login/', views.user_login, name='user_login'),
    path('fb_registration/', views.user_register, name='user_register'),
    path('fb_updatePassword/', views.updatePassword, name='update_password'),
    path('fb_insert_post/', views.insert_post, name='insert_post'),
    path('fb_delete_post/', views.delete_post, name='delete_post')
]

from django.contrib import admin
from django.urls import path
from rules_app import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home),
    path('index',views.index),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('about',views.about),
]

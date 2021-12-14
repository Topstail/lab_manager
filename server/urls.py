from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('show_hosts', views.show_all_host),
    path('show_dashboard', views.show_dashboard),
    path('add_host', views.add_host),
]


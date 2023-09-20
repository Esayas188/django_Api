
from . import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('drinks',views.Listdrinks.as_view(), name='home'),
    path('drinks/<int:pk>',views.DetailDrinks.as_view(), name='home')


]

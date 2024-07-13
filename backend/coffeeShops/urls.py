from django.urls import path
from . import views

urlpatterns = [
    path('', views.coffee_shop_list, name='coffee_shop_list'),
]
from django.shortcuts import render
from .models import CoffeeShop

def coffee_shop_list(request):
    coffee_shops = CoffeeShop.objects.all()
    return render(request, 'coffeeShops/coffee_shop_list.html', {'coffee_shops': coffee_shops})
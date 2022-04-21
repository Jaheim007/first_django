from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

def index(request):  
    # world = Pizza.objects.all() 
    # pizza_names = [pizza.nom + ":" + str(pizza.price) + "£" for pizza in world]
    # pizza_names_str =" ,".join(pizza_names)  
    # return HttpResponse("Les Pizza: " + pizza_names_str) 
    pizzas = Pizza.objects.all() 
    return render(request, 'menu/index.html', locals())

def too(request):      
    return HttpResponse("Hello World")


def main(requests):    
    return render(requests, 'menu/main.html', locals() )
from re import search
from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):      
    list_display = ('nom', 'ingerdients', 'price', 'vegetrian')
    search_fields = ['nom']
admin.site.register(Pizza, PizzaAdmin)

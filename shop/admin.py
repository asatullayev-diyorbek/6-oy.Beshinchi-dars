from django.contrib import admin
from .models import Product

@admin.register(Product)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('name', 'price')
    search_fields = ('name', 'price')




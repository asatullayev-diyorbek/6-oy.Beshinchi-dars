from django.shortcuts import render
from django.views.generic import View
from .models import Product


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'title': 'Mahsulotlar',
            'products': products
        }
        return render(request, 'index.html', context)

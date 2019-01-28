from django.shortcuts import render
from .models import Product
# Create your views here.


def product_detail_view(request):

    obj = Product.objects.get(id=4)

    context = {
        'obj': obj
    }

    return render(request, "products/product_detail.html", context)

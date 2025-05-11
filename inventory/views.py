from django.shortcuts import get_object_or_404, render

from inventory.models import Inventory

def index(request):
    items = Inventory.objects.all()

    context = {
        'items': items
    }

    return render(request, 'store/index.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Inventory, pk=pk)

    context = {
        'product': product
    }

    return render(request, 'store/product.html', context)
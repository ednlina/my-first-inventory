from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Inventory

# Create your views here.
def inventory_list(request):
    #items = Inventory.objects.filter(title__contains='chair')
    items = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def inventory_detail(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'item': item})

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Inventory
from .forms import InventoryForm

# Create your views here.
def inventory_list(request):
    #items = Inventory.objects.filter(title__contains='chair')
    items = Inventory.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def inventory_detail(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'item': item})

#def inventory_new(request):
#    form = InventoryForm()
#    return render(request, 'inventory/inventory_edit.html', {'form': form})

def inventory_new(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.published_date = timezone.now()
            item.save()
            return redirect('inventory_detail', pk=item.pk)
    else:
        form = InventoryForm()
    return render(request, 'inventory/inventory_edit.html', {'form': form})

def inventory_edit(request, pk):
    item = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.published_date = timezone.now()
            item.save()
            return redirect('inventory_detail', pk=item.pk)
    else:
        form = InventoryForm(instance=item)
    return render(request, 'inventory/inventory_edit.html', {'form': form})

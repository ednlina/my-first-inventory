from django.shortcuts import render

# Create your views here.
def inventory_list(request):
    return render(request, 'inventory/inventory_list.html', {})

from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.


def home(request):
    return render(request, 'products/home.html')


def item(request, item_id):
    item_info = get_object_or_404(Item, pk=item_id)
    return render(request, 'products/item.html', {'item': item_info})

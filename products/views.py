from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
# Create your views here.


def home(request):
    items = Item.objects
    return render(request, 'products/home.html', {'items': items})


def item(request, item_id):
    item_info = get_object_or_404(Item, pk=item_id)
    return render(request, 'products/item.html', {'item': item_info})


@login_required(login_url='/accounts/signup')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon'] and request.POST['text']:
            item_object = Item()
            item_object.title = request.POST['title']
            item_object.text = request.POST['text']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                item_object.url = request.POST['url']
            else:
                item_object.url = 'http://'+request.POST['url']
            item_object.icon = request.FILES['icon']
            item_object.image = request.FILES['image']
            item_object.user = request.user
            item_object.save()
            return redirect('/products/' + str(item_object.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'products/create.html')


@login_required(login_url='/accounts/signup')
def upvote(request, item_id):
    if request.method == 'POST':
        item_object = get_object_or_404(Item, pk=item_id)
        item_object.votes_total += 1
        item_object.save()
        return redirect('/products/' + str(item_object.id))
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *



def must_have(request):
    global order, items, cartItems
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.ordereditem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items' : 0, 'get_cart_total' : 0}
        cartItems = order['get_cart_items']

# Create your views here.
def store_view(request):
    products = Product.objects.all()
    must_have(request)
    context = {'products' : products, 'cartItems' : cartItems}
    return render(request, 'store/store.html', context)

def cart_view(request):
    must_have(request)
    context = {'items' : items, 'order' : order, 'cartItems' : cartItems}
    return render(request, 'store/cart.html', context)

def checkout_view(request):
    must_have(request)
    context = {'items' : items, 'order' : order, 'cartItems' : cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem_view(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print(f'Id = {productId},   action = {action}')

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderedItems, created = OrderedItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderedItems.quantity = (orderedItems.quantity + 1)
    elif action == 'remove':
        if orderedItems.quantity <= 0:
            orderedItems.delete()
        else:
            orderedItems.quantity = (orderedItems.quantity - 1)

    orderedItems.save()

    if orderedItems.quantity == 0:
        orderedItems.delete()

    return JsonResponse('Item was added successfuly', safe=False)

from django.urls import path
from .views import *

urlpatterns = [
    path('', store_view, name="store"),
    path('cart/', cart_view, name="cart"),
    path('checkout/', checkout_view, name="checkout")
]

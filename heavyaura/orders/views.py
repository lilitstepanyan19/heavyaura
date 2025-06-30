from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView

from cart.cart import Cart

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST, request=request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            cart.clear()
            return render(request, 'order/created.html', 
                {'order' : order,
                 'form' : form}
            )
    else:
        form = CreateOrderForm(request=request)
    return render(request, 'order/created.html', 
                {'order' : order,
                 'form' : form}
            )
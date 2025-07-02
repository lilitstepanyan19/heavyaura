from django.shortcuts import render, redirect
from django.urls import reverse
from orders.models import OrderItem
from orders.forms import OrderCreatedForm
from cart.cart import Cart



def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreatedForm(data=request.POST, request=request)
        if form.is_valid():
            order = form.save()
            for item in cart:
                discounted_price = item['product'].sell_price()
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=discounted_price,
                                         quantity=item['quantity'])
            
            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreatedForm(request=request)
    return render(request, 'orders/create.html', 
                {'cart' : cart,
                 'form' : form})
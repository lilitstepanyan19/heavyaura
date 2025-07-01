from django.shortcuts import render
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
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            cart.clear()
            return render(request, 'orders/created.html', 
                {'order' : order,
                 'form' : form}
            )
    else:
        form = OrderCreatedForm(request=request)
    return render(request, 'orders/create.html', 
                {
                 'form' : form})
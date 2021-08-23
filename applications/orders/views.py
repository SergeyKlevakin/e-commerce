from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreatedForm
from applications.carts.cart import Cart


def order_create(request):
    cart = Cart(request)
    form = OrderCreatedForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            order = form.save()
            for item in cart:
                product_item = item['product']
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                product_item.quantity -= item['quantity']
                product_item.save()
            cart.clear()
            return render(request, 'orders/order/created.html', context={'order': order})
        else:
            form = OrderCreatedForm()
    return render(request, 'orders/order/create.html', context={'cart': cart, 'form': form})




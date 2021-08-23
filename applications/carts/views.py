from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from applications.shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.http import HttpResponse


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        if product.quantity < form.cleaned_data['quantity']:
            return HttpResponse(f'Нет такого колличества товара! Доступно {product.quantity}')
        cart.add(product=product, quantity=form.cleaned_data['quantity'], update_quantity=form.cleaned_data['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', context={'cart': cart})

from .cart import Cart


def cart(request):
    return {'cart_item': Cart(request)}

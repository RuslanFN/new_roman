from django.shortcuts import render, redirect
from cart.cart import Cart
from django.views.decorators.http import require_GET, require_POST
from shop.views import get_construct
@require_POST

def cart_add(request):
    cart = Cart(request)
    textileId = request.POST.get('textile-id')
    lenght = request.POST.get('height')
    width = request.POST.get('width')
    kantId = request.POST.get('kant-id')
    side_chain = request.POST.get('side-chain')
    if not textileId or not kantId:
        return redirect("construct")
    cart.add(textile=textileId, lenght=lenght,
        width=width, kantId=kantId,
        side_chain=side_chain)
    return redirect("construct")
def get_cart(request):
    cart = Cart(request)
    print(cart.cart)
    is_moderator = request.user.groups.filter(name='moderator').exists()
    return render(request, "cart.html", {"cart": cart, 'is_moderator': is_moderator})
def remove(request):
    cart = Cart(request)
    if str(request.GET.get('id')).isdigit():
        id = int(request.GET.get('id'))
        cart.remove(id)
    return redirect('cart')


from django.shortcuts import render, HttpResponse, redirect
from shop.models import Textile, Kant, Order, Rome_Blind, Side_Chain
from django.contrib.auth import authenticate, login, logout
from cart.cart import Cart


def make_order(request):
    if request.POST:
        cart = Cart(request)
        adress = request.POST.get('adress')
        tel = request.POST.get('tel')
        order = Order.objects.create(adress=adress, number=tel)
        for item in cart:
            try:
                textile = Textile.objects.get(id=item.get('textileId'))
                kant = Kant.objects.get(id=item.get('kantId'))
                side = item.get('side_chain')
                if side == 'Right':
                    side = Side_Chain.Right
                else:
                    side = Side_Chain.Left
                    width = item.get('width')
                    height = item.get('lenght')
                Rome_Blind.objects.create(Textile=textile, Kant=kant, width=width, height=height, side_chain=side, order=order)
                
            except Exception:
                return redirect('construct')
        cart.remove_all()
        return redirect('construct')
    is_moderator = request.user.groups.filter(name='moderator').exists()
    return render(request, 'shop/Order.html',{'is_moderator':is_moderator})

def detail_order(request):
    if request.user.groups.filter(name='moderator').exists():
        is_moderator = request.user.groups.filter(name='moderator').exists()
        id = request.GET.get('id')
        if not str(id).isdigit():
            return HttpResponse(f"Пользователь не найден {str(id)}", status=404)
        order = Order.objects.get(id=int(id))
        blinds = Rome_Blind.objects.all().filter(order=order)
        print(blinds.all())
        return render(request, 'shop/order_detail.html', {'blinds':blinds, 'is_moderator':is_moderator})
    else:
        return HttpResponse(status=404)

def remove_order(request):
    if request.user.groups.filter(name='moderator').exists():
        id = request.GET.get('id')
        if not str(id).isdigit():
            
            return HttpResponse(f"Пользователь не найден {str(id)}", status=404)
        Order.objects.get(id=int(id)).delete()
        return redirect('orders')
    else:
        return HttpResponse(status=404)

def get_orders(request):
    if request.user.groups.filter(name='moderator').exists():
        is_moderator = request.user.groups.filter(name='moderator').exists()
        orders = Order.objects.all().order_by('date')
        print(orders)
        return render(request, 'shop/orders_list.html', {'orders':orders, 'is_moderator':is_moderator})
    else:
        return HttpResponse(status=404 )

def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('construct')
        else:
            return HttpResponse("Пользователь не найден", status=404)
    return render(request, 'shop/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('construct')
    return HttpResponse(status=404)

def get_construct(request):
    is_moderator = request.user.groups.filter(name='moderator').exists()
    textile = Textile.objects.all()
    kants = Kant.objects.all()
    return render(request, "shop/construct.html", {'textiles': textile, 'Kants':kants, 'is_moderator': is_moderator})

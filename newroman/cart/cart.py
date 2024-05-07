from django.conf import settings
from shop.models import Textile, Kant
class Cart(object):
    def __init__(self, request):
        self.max_ind = 0
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = []
        self.cart = cart
    def add(self, textile, lenght, width, kantId, side_chain):
        product = {'ind':self.max_ind+1, 'textileId':textile, 'lenght': lenght, 'width':width, 'kantId':kantId, 'side_chain':side_chain}
        self.max_ind += 1
        self.cart.append(product)
        self.save()
    def remove_all(self):
        self.cart.clear()
        self.save
    def remove(self, ind):
        for i in range(len(self.cart)):
            if self.cart[i].get('ind') == ind:   
                self.cart.pop(i)
                break
        self.save()
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
    def __iter__(self):
        items = self.cart
        for item in items:
            yield item
    def __len__(self):
        return len(self.cart)

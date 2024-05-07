"""
URL configuration for newroman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import get_construct, user_login, user_logout, make_order
from django.conf import settings
from cart.views import cart_add, get_cart,remove
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('construct/', get_construct, name='construct'),
    path('construct/add', cart_add),
    path('cart', get_cart, name='cart'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('order/', make_order, name='order'),
    path('remove/', remove, name='remove'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

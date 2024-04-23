from django.contrib import admin
from shop.models import Textile, Order

admin.site.Register(Order)
admin.site.Register(Textile)
# Register your models here.

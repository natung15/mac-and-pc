from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
#this displays the name price stock in the admin page 

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
#this is to add a line to the admin site administration
#basically updates the info on the page


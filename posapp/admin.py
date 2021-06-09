from django.contrib import admin
from .models.product import Product
from .models.customer import Customer

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Customer)

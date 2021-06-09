from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from posapp.models.product import Product
from posapp.models.customer import Customer
from django.views import View

# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        print(product)
        return redirect('homepage')


    def get(self, request):
        cart = request.session.get('cart')
        products = None
        if not cart:
            request.session['cart'] = {}
        products = Product.get_all_products();
        data = {}
        data['products'] = products
        print(products)
        print('you are:', request.session.get('email'))
        return render(request, 'test.html', data)
        # return render(request, 'orders/order.html')



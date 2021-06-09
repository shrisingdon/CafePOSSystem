from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from posapp.models.product import Product
from posapp.models.customer import Customer
from django.views import View



class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "email or password invalid"
        else:
            error_message = "email or password invalid"
        return render(request, 'login.html', {'error': error_message})


def Logout(request):
    request.session.clear()
    return redirect('login')


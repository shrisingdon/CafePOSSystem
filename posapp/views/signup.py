from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from posapp.models.product import Product
from posapp.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password((customer.password))

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "first name required"
        elif len(customer.first_name) < 4:
            error_message = "less than 4 characters"
        elif (not customer.last_name):
            error_message = "last name required"
        elif len(customer.last_name) < 4:
            error_message = "less than 4 characters"
        elif not customer.phone:
            error_message = "Phone number required"
        elif len(customer.phone) < 10:
            error_message = "less than 10 characters"
        elif customer.isExists():
            error_message = "Email already exists"

        return error_message


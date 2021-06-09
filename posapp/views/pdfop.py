from django.http import HttpResponse, HttpResponseRedirect, FileResponse, request
from django.shortcuts import render
from django.views import View
from .utils import render_to_pdf  # created in step 4

from posapp.models import Product


class Pdf(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'pdf-output.html', {'products': products})


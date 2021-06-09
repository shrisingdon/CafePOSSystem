from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from posapp.models.product import Product

class CustomerListView(ListView):
    model = Product
    template_name = 'pdf-output.html'

def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    product = get_object_or_404(Product, pk=pk)
    template_path = 'pdf-output.html'
    context = {'posapp': product}
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
    html = template.render(context)



def render_pdf_view(request):
    template_path = 'pdf-output.html'
    context = {}
    response = HttpResponse(content_type='application/pdf')
    template = get_template(template_path)
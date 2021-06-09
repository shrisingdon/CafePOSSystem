from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View

from .utils import render_to_pdf #created in step 4
from ..models import Product
from ..templatetags.cart import cart_quantity, price_total


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf-output.html')
        ids = list(request.session.get('cart').keys())
        context = {
            'id': {ids},
            'product.name': {{Product.get_products_by_id(ids)}},
            'Price': {{Product.price}},
            'Quantity': {{Product|cart_quantity:request.session.cart}},
            'Total': {{Product|price_total:request.session.cart}}
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf-output.html')
        return HttpResponse(pdf, content_type='application/pdf')
        # return pdf
#
#     # 'id': {ids},
#     # 'Product': {{Product.get_products_by_id(ids)}},
#     # 'Price': {{Product.price}},
#     # 'Quantity': {{Product | cart_quantity: request.session.cart}},
#     # 'Total': {{Product | price_total: request.session.cart}}

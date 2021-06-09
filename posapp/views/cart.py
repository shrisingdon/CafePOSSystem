import pdfkit
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, request
# from django.contrib.auth.hashers import make_password, check_password
# from django.urls import path
#
# from posapp.models.product import Product
# from posapp.models.customer import Customer
# from django.template import Context
from django.views import View

from posapp.models import product
from posapp.models.product import Product
# from django.template.loader import render_to_string
# import tempfile
# from django.db.models import Sum
# import pdfkit
from io import BytesIO
# from reportlab.pdfgen import canvas
# from django.core.files.storage import FileSystemStorage
# from weasyprint import HTML
# from posapp.templatetags.cart import cart_quantity, price_total
# from posapp.utils import render_to_pdf
from django.template.loader import get_template
# import datetime
from xhtml2pdf import pisa


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request, 'cart.html', {'products':products})


# def invoicepdf(request, d):
#     config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
#     pdfkit.from_url(request.get_host() + '/%s' % d, 'media/invoice/%s.pdf' % d, configuration=config,options=options)
#     return HttpResponseRedirect('/%s.pdf' % d)



# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#
#     # This part will create the pdf.
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None


# def getpdfPage(request):
#     template = io.BytesIO()
#     p = canvas.Canvas(template)
#
#     p.drawString(100, 100, "Hello world.")
#
#     p.showPage()
#     p.save()
#
#     template.seek(0)
#     return FileResponse(template, as_attachment=True, filename='hello.pdf')
#
#     buffer = io.BytesIO()
#
#     # Create the PDF object, using the buffer as its "file."
#     p = canvas.Canvas(buffer)
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     p.drawString(100, 100, "Hello world.")
#
#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()
#
#     # FileResponse sets the Content-Disposition header so that browsers
#     # present the option to save the file.
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
#     response['Content-Disposition'] = 'attachment; filename-Expenses' + \
#         str(datetime.datetime.now()) + '.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'
#
#     html_string = render_to_string('templates/cart')
#     html = HTML(string = html_string)
#
#     result = html.write_pdf()
#
#     with tempfile.NamedTemporaryFile(delete = True) as output:
#         output.write(result)
#         output.flush()
#
#         output = open(output.name, 'rb')
#         response.write(output.read())
#
#     return response




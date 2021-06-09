"""POScafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, Logout
from .views.cart import Cart
from .views.GeneratePdf import GeneratePdf
from .views.pdfop import Pdf
# from .views.dy import CustomerListView, render_pdf_view, customer_render_pdf_view

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    url(r'^pdf/&', GeneratePdf.as_view(), name='GeneratePdf'),
    # path('', CustomerListView.as_view(), name='customer-list-view'),
    # path('test/', render_pdf_view, name='test-view'),
    # path('pdf/<pk>/', customer_render_pdf_view, name='customer_pdf-view')
    # path('GeneratePdf', Pdf.as_view(), name='GeneratePdf'),
    path('pdfop', Pdf.as_view(), name='pdfop'),
    # path('getpdfPage', getpdfPage, name='getpdfPage')
]

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
from django.urls import path, include

# from posapp.views.GeneratePdf import Pdf
from posapp.views.GeneratePdf import GeneratePdf
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posapp.urls')),
    # url(r'^pdf/&', GeneratePdf.as_view()),
    # path('GeneratePdf', Pdf.as_view(), name='GeneratePdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

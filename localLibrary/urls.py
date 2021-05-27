"""localLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include #new1
from django.views.generic import RedirectView #new2
from django.conf import settings #new3
from django.conf.urls.static import static #new3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')), #new1
    path('', RedirectView.as_view(url='/catalog/')), #new2
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #new3

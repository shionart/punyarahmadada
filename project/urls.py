"""project URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from indonesia.viewset_api import *
from rest_framework import routers
from indonesia.views import indeks, detail, tabeel, coba, koef, insertDb

router =routers.DefaultRouter()
router.register('Power/', PowerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('indeks/', indeks),
    path('indeks/detail', detail),
    path('indeks/tabeel', tabeel),
    path('indeks/coba', coba),
    path('indeks/koef', koef),
    path('insertDb', insertDb),
]

"""
URL configuration for carfix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from carfix import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about/', views.about , name='about'),
    path('services/', views.services , name='services'),
    path('contect/', views.contect , name='contect'),
    path('review/', views.review , name='review'),
    path('caseList/', views.caseList , name='caseList'),
    path('caseDetail/', views.caseDetail , name='caseDetail'),
    path('ourTeam/', views.ourTeam , name='ourTeam'),
    path('shp/', views.shop , name='shop'),
    path('products/', views.products , name='products'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('login/', views.login , name='login')
    # path('home', views.home),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
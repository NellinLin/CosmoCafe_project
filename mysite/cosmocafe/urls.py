from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings as set
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    #path('', views.index, name="index"),
    path('menufull/', views.menufull, name="menufull" ),
    path('cupcakes/', views.cupcakes, name="cupcakes" ), #кексы
    path('macaroons/', views.macaroons, name="macaroons" ), # макаруны
    path('cakes/', views.cakes, name="cakes" ), # пирожные
    path('drinks/', views.drinks, name="drinks" ), # напитки
    path('menu/', views.menu, name="menu" ),

    path('', views.index, name="index"),
    path('aboutus/', views.aboutus, name="aboutus" ),
    path('contacts/', views.contacts, name="contacts" ),
    path('photogalery/', views.photogalery, name="photogalery" ),
    path('writeus/', views.writeus, name="writeus" ),
]

if set.DEBUG:
    urlpatterns += static(set.STATIC_URL, document_root = set.STATIC_ROOT)
    urlpatterns += static(set.MEDIA_URL, document_root=set.MEDIA_ROOT)
import imp
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import create_update, home,register,booklist
from django.conf.urls.static import static
from libmanagement import settings
urlpatterns = [
         path('',home),
         path('register',register),
        path('book/list',booklist),
         path('book/create-update',create_update), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
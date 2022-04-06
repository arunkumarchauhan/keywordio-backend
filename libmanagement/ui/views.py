from django.shortcuts import render

from rest_framework import response, decorators, permissions, status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer



def home(request):
    return render(request, 'index2.html', status=status.HTTP_200_OK)

def register(request):
    return render(request, 'register.html', status=status.HTTP_200_OK)



def booklist(request):
    return render(request, 'viewbook.html', status=status.HTTP_200_OK)    

def create_update(request):
    return render(request, 'create_update.html', status=status.HTTP_200_OK)      
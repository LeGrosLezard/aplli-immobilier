"""There is views from model MVC"""

from django.shortcuts import render


def home(request):
    """Home template"""
    return render(request, 'home.html')





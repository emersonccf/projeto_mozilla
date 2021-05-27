from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_view(request):
    return HttpResponse("<h1>LocalLibrary - Seja bem-vindo</h1>")

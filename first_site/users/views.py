from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def sign_in(request):
    return HttpResponse("<h1>Login</h1>")

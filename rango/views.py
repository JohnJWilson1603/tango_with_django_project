from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Rango says hey there partner!")

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def advantages(request):
    return render(request, 'advantages.html')

def prices(request):
    return render(request, 'prices.html')

def faqs(request):
    return render(request, 'faqs.html')

def about(request):
    return render(request, 'about.html')
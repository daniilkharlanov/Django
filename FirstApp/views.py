from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(recuest):
    return HttpResponse('<h1> Приветствую вас на первом в мире сатйе, который построен человеком, а не компьютером.</h1>')
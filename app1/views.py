from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample1(request):
    return HttpResponse('Hai Hello')

def sample2(request):
    return HttpResponse('hai jyothi')
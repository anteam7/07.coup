from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>hello, world!</h1>')


def main(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')    
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>hello, world!</h1>')


def main(request):
    return render(request, 'main.html')

def category(request):
    return render(request, 'category.html')    


def path(request):
    page = request.GET['page']

    html_path = "main.html"
    if page == "게이밍모니터최저가":
        html_path = "monitor.html"

    return render(request, html_path, {'page_data':page})       

def front(request):
    return render(request, 'front/webtest.html')
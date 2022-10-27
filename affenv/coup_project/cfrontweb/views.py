from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
#    return HttpResponse('<h1>hello, front web world!</h1>')
    return render(request, 'front/curation_main.html')
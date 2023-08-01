from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def view_index(request):
    html = "<h1>这个是Poll页面</h1>"
    return HttpResponse(html)
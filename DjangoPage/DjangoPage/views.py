from django.http import HttpResponse

def view_index(request):
    html = "<h1>这个是主页面</h1>"
    return HttpResponse(html)

def view_page1(request):
    html = "<h1>第一个页面</h1>"
    return HttpResponse(html)
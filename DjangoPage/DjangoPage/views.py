from django.http import HttpResponse

def view_index(request):
    html = "<h1>这个是主页面</h1>"
    return HttpResponse(html)


def view_page(request, pg):
    html = "<h1>这是第%s个页面</h1>"%(pg)
    return HttpResponse(html)
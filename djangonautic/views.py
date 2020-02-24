from django.http import HttpResponse

def homepage (resquest):
    return HttpResponse('Homepage')

def about (request):
    return HttpResponse('about')
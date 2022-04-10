from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def list_HERO11(request):
    return HttpResponse('Dr Nice')

def list_HERO12(request):
    return HttpResponse('necromancer')

def list_HERO13(request):
    return HttpResponse('Bombasto')

def list_HERO14(request):
    return HttpResponse('Celeritas')

def list_HERO15(request):
    return HttpResponse('Magneta')

def list_HERO16(request):
    return HttpResponse('RubberMan')

def list_HERO17(request):
    return HttpResponse('Dynama')

def list_HERO18(request):
    return HttpResponse('Dr IQ')

def list_HERO19(request):
    return HttpResponse('Magma')

def list_HERO20(request):
    return HttpResponse('Tornado')


def Myherois(request):
    return HttpResponse('Dr Nice')




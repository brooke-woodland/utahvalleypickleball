from django.http import HttpResponse

def indexPageView(request):
    return HttpResponse('Homepage')

def aboutPageView(request):
    return HttpResponse('About Page')

def mapsPageView(request):
    return HttpResponse('Map Page')

def dataPageView(request):
    return HttpResponse('Data Page')
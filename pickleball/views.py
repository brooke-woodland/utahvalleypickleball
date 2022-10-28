from django.http import HttpResponse

def indexPageView(request):
    """
    This is the landing page
    """
    return HttpResponse('Homepage')

def aboutPageView(request):
    """
    This is the about page
    """
    return HttpResponse('About Page')

def mapsPageView(request):
    """
    This is the maps page
    """
    return HttpResponse('Map Page')

def dataPageView(request):
    """
    This is the data page
    """
    return HttpResponse('Data Page')
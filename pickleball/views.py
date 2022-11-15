from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request):
    """
    This is the landing page
    """
    return render(request, 'pickleball/index.html')

def aboutPageView(request):
    """
    This is the about page
    """
    return render(request, 'pickleball/about.html')

def mapsPageView(request):
    """
    This is the maps page
    """
    return render(request, 'pickleball/map.html')

def dataPageView(request):
    """
    This is the data page
    """
    return render(request, 'pickleball/data.html')
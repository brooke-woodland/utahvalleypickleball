from django.http import HttpResponse
from django.shortcuts import render
import googlemaps

from models import Location

# import asyncio
from json import dumps

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
    gmaps = googlemaps.Client(key="AIzaSyA1QLwVy_gy2FPUh4v6_ly1CqmtUkk7IAw")

    locationData = Location.objects.all()

    # sampleData = [
    #     {
    #         "address": "600 North 300 East",
    #         "city": "Orem",
    #         "state": "UT"
    #     },
    #     {
    #         "address": "575 W Center St",
    #         "city": "Orem",
    #         "state": "UT"
    #     },
    #     {
    #         "address": "320 500 N",
    #         "city": "Provo",
    #         "state": "UT"
    #     },
    # ]

    coordinateArray = []

    for data in locationData:
        geocode_result = gmaps.geocode(f"{data['street_address']}, {data['city']}, {data['state']}")

        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        coordinateArray.append({ "lat": latitude, "lng": longitude })

    coordinateArray = dumps(coordinateArray)

    context = {
        "data": coordinateArray
    }

    return render(request, 'pickleball/map.html', context)

def dataPageView(request):
    """
    This is the data page
    """
    return render(request, 'pickleball/data.html')
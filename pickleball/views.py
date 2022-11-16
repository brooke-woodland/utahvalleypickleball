from django.http import HttpResponse
from django.shortcuts import render
import googlemaps
from json import dumps
import environ

env = environ.Env()

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
    key = env('GOOGLE_MAPS_API_KEY')

    gmaps = googlemaps.Client(key=key)

    sampleData = [
        {
            "street_address": "600 North 300 East",
            "city": "Orem",
            "state": "UT"
        },
        {
            "street_address": "575 W Center St",
            "city": "Orem",
            "state": "UT"
        },
        {
            "street_address": "320 500 N",
            "city": "Provo",
            "state": "UT"
        },
    ]

    coordinateArray = []

    for data in sampleData:
        geocode_result = gmaps.geocode(f"{data['street_address']}, {data['city']}, {data['state']}")

        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        coordinateArray.append({ "lat": latitude, "lng": longitude })

    coordinateArray = dumps(coordinateArray)

    context = {
        "data": coordinateArray,
        "key": key
    }

    return render(request, 'pickleball/map.html', context)

def dataPageView(request):
    """
    This is the data page
    """
    return render(request, 'pickleball/data.html')
from django.http import HttpResponse
from django.shortcuts import render, redirect
import googlemaps
from json import dumps
import environ
from .models import Location

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
    # Grab api key
    key = env('GOOGLE_MAPS_API_KEY')

    # Initialize maps client
    gmaps = googlemaps.Client(key=key)

    # Grab all locations
    locations = Location.objects.defer("court_name", "courts", "openTime", "closeTime", "indoor").values()

    # Initialize coordinate array
    coordinateArray = []

    # Loop through locations, converting address to coordinates
    for data in locations:

        # Convert to coordinates
        geocode_result = gmaps.geocode(f"{data['street_address']}, {data['city']}, {data['state']}")

        # Save lat and long
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']

        # Update array
        coordinateArray.append({ "lat": latitude, "lng": longitude })

    # Dump it to json
    coordinateArray = dumps(coordinateArray)

    # Set context
    context = {
        "data": coordinateArray,
        "key": key
    }

    return render(request, 'pickleball/map.html', context)

def dataPageView(request):
    """
    This is the data page
    """
    # Grab all location objects
    locations = Location.objects.all().values()

    # Convert time to string
    for location in locations:
        location['openTime'] = location['openTime'].strftime("%H:%M:%S")
        location['closeTime'] = location['closeTime'].strftime("%H:%M:%S")

    # Set context
    context = {
        "data": locations
    }

    return render(request, 'pickleball/data.html', context)


def addDataPageView(request):
    """
    This is the add data page
    """
    return render(request, 'pickleball/addData.html')

def addData(request):
    """
    This adds new data
    """
    # Grab body from request
    body = dict(request.POST.items())

    # Grab params
    court_name = body['court_name']
    street_address = body['street_address']
    city = body['city']
    state = body['state']
    courts = int(body['courts'])
    openTime = body['openTime']
    closeTime = body['closeTime']
    indoor = True if body['indoor'] == 'True' else False

    # Create new object
    newLocation = Location(
        court_name=court_name,
        street_address=street_address,
        city=city,
        state=state,
        courts=courts,
        openTime=openTime,
        closeTime=closeTime,
        indoor=indoor
    )

    # Save it
    newLocation.save()

    return redirect('/data/view')


def updateDataPageView(request):
    """
    This is the update data page
    """
    # Grab body from request
    body = dict(request.POST.items())

    # Set context
    context = {
        "court_name": body['court_name'],
        "street_address": body['street_address'],
        "city": body['city'],
        "state": body['state'],
        "courts": int(body['courts']),
        "openTime": body['openTime'],
        "closeTime": body['closeTime'],
        "indoor": True if body['indoor'] == 'True' else False,
        "id": int(body['id'])
    }

    return render(request, 'pickleball/updateData.html', context)


def updateData(request):
    """
    This updates data
    """
    # Grab body from request
    body = dict(request.POST.items())

    # Grab location object
    location = Location.objects.get(id=body['id'])

    # Update items
    location.court_name = body['court_name']
    location.street_address = body['street_address']
    location.city = body['city']
    location.state = body['state']
    location.courts = int(body['courts'])
    location.openTime = body['openTime']
    location.closeTime = body['closeTime']
    location.indoor = True if body['indoor'] == 'True' else False

    # Save it
    location.save()

    return redirect('/data/view')


def deleteData(request):
    """
    This deletes data
    """
    # Grab body from request
    body = dict(request.POST.items())

    # Grab location object by id
    location = Location.objects.get(id=body['id'])

    # Delete it
    location.delete()

    return redirect('/data/view')
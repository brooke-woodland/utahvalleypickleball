from django.urls import path
from .views import indexPageView, aboutPageView, mapsPageView, dataPageView

urlpatterns =[
    path ("", indexPageView, name ="index"),
    path('about/', aboutPageView, name='about'),
    path('data/', dataPageView, name='data'),
    path('maps/', mapsPageView, name='maps'),
]
from django.urls import path
from .views import indexPageView, aboutPageView, mapsPageView, dataPageView
from .views import addDataPageView, updateDataPageView, deleteData, updateData

urlpatterns =[
    path('about/', aboutPageView, name='about'),
    path('data/view', dataPageView, name='data'),
    path('data/add', addDataPageView, name='addData'),
    path('data/update', updateDataPageView, name='updateData'),
    path('data/update/save', updateData, name='updateDataSave'),
    path('data/delete', deleteData, name='deleteData'),
    path('maps/', mapsPageView, name='maps'),
    path ("", indexPageView, name ="index"),
]
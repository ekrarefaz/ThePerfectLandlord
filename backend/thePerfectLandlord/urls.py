from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myproperties', views.myproperties, name="myproperties"),
    path('property/<int:id>', views.property, name="property"),
    path('property/<int:id>/details', views.propertydetails, name="propertydetails"),
    path('property/<int:id>/details/update', views.propertyupdate, name="propertyupdate"),
]
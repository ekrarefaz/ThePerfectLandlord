from django.urls import path

from . import views
from thePerfectLandlord import views as site_views

urlpatterns = [
    
]
urlpatterns = [
    path('', site_views.vue_test),
    # path('myproperties', views.myproperties, name="myproperties"),
    # path('property/<int:id>', views.property, name="property"),
    # path('property/<int:id>/details', views.propertydetails, name="propertydetails"),
    # path('property/<int:id>/details/update', views.propertyupdate, name="propertyupdate"),
]
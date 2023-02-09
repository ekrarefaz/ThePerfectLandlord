from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import *
def vue_test(request):
    return render(request, 'vue-test.html')

# def validate(user, role):
#     for g in user.groups.all():
#         if g.name == role:
#             return True
#     return False

# @login_required
# def index(request):
#     if validate(request.user, 'Landlord'):
#         return render(request, 'landlord/homepage.html')
    
#     return render(request, 'login.html')

# @login_required
# def myproperties(request):
#     try:
#         # Retrieve all properties registered with the user id
#         my_properties = Property.objects.filter(landlord_id=request.user)
    
#     except:
#         my_properties = []

#     # Send the list of properties to front
#     return render(request, 'landlord/myproperties.html', {'my_properties': my_properties})

# @login_required
# def property(request, id):
#     # Return navigation
#     return render(request, 'landlord/property.html', {'property_id': id})

# @login_required
# def propertydetails(request, id):
#     try:
#         # Retrieve the property selected
#         property = Property.objects.get(property_id=id)
    
#     except:
#         property = {}

#     # Send the property object to front
#     return render(request, 'landlord/propertydetails.html', {'property' : property})

# @login_required
# def propertyupdate(request, id):
#     # Retrieve user inputs
#     address = request.POST['address']
#     desc = request.POST['desc']
#     weekly_price = int(request.POST['weekly_price'])

#     try:
#         # Retrieve the property selected
#         p = Property.objects.get(property_id=id)

#     except Property.DoesNotExist:

#         # Create property with the input values
#         p = Property()
    
#     finally:
#         # Assign values into the property
#         p.address = address
#         p.desc = desc
#         p.weekly_price = weekly_price
#         p.save()

#     return render(request, 'landlord/propertydetails.html', {'property' : p})
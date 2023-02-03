from datetime import date, datetime
from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

# Helper Classes

class ResidentialType(models.Model):
    type_id=models.BigAutoField(primary_key=True)
    type_name= models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.type_name
    
    def getId(self):
        return self.type_id

class IncomeType(models.Model):
    type_id=models.BigAutoField(primary_key=True)
    type_name= models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.type_name
    
    def getId(self):
        return self.type_id

class IdentityType(models.Model):
    type_id=models.BigAutoField(primary_key=True)
    type_name= models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.type_name
    
    def getId(self):
        return self.type_id

class PropertyType(models.Model):
    type_id=models.BigAutoField(primary_key=True)
    type_name= models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.type_name
    
    def getId(self):
        return self.type_id

class Frequency(models.Model): #added
    freq_id=models.BigAutoField(primary_key=True)
    freq_name= models.CharField(max_length=20, blank=False)    

class Document(models.Model):
    doc_id=models.BigAutoField(primary_key=True)
    doc_path= models.CharField(max_length=30, blank=False)

# User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    age= models.IntegerField(default=0, blank=True)

# User Residential

class ResidentialItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    residential_type_id = models.ForeignKey(ResidentialType, null=True, blank=False, on_delete = models.SET_NULL)
    address = models.CharField(max_length=30, blank=False)
    start_date = models.DateField(auto_now_add=True, blank=False)
    end_date = models.DateField(auto_now_add=True, blank=True)
    reference_name = models.CharField(max_length=20, blank=False)
    reference_phone = models.IntegerField(default=0, blank=False)
    reference_email = models.EmailField(max_length=30, blank=True)

class ResidentialDetail(models.Model):
    details_id = models.BigAutoField(primary_key=True) 
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    item_id = models.ForeignKey(ResidentialItem, on_delete = models.CASCADE)
    verified = models.BooleanField(default=False, blank=False)

# User Employment

class EmploymentItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    company = models.CharField(max_length=30, blank=False)
    start_date = models.DateField(auto_now_add=True, blank=False)
    end_date = models.DateField(auto_now_add=True, blank=True)
    role = models.CharField(max_length=20, blank=False)
    reference_name = models.CharField(max_length=20, blank=False)
    reference_phone = models.IntegerField(default=0, blank=False)
    reference_email = models.EmailField(max_length=30, blank=True)

class EmploymentDetail(models.Model):
    details_id = models.BigAutoField(primary_key=True) 
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    item_id = models.ForeignKey(EmploymentItem, on_delete = models.CASCADE)
    verified = models.BooleanField(default=False, blank=False)

# User Income

class IncomeItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    income_type_id = models.ForeignKey(IncomeType, null=True, blank=False, on_delete = models.SET_NULL)
    frequency_id = models.ForeignKey(Frequency, null=True, blank=False, on_delete = models.SET_NULL)
    income_doc_id = models.ForeignKey(Document, null=True, blank=False, on_delete = models.SET_NULL)
    amount= models.IntegerField(default=0, blank=False)
    
class IncomeDetail(models.Model):
    details_id = models.BigAutoField(primary_key=True) 
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    item_id = models.ForeignKey(IncomeItem, on_delete = models.CASCADE)
    verified = models.BooleanField(default=False, blank=False)

# User Identity

class IdentityItem(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    identity_type = models.ForeignKey(IdentityType, null=True, blank=False, on_delete = models.SET_NULL)
    identity_doc_id = models.ForeignKey(Document, null=True, blank=False, on_delete = models.SET_NULL)
    
class IdentityDetail(models.Model):
    details_id = models.BigAutoField(primary_key=True) 
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    item_id = models.ForeignKey(IdentityItem, on_delete = models.CASCADE)
    verified = models.BooleanField(default=False, blank=False)

# Property

class Property(models.Model):
    property_id = models.BigAutoField(primary_key=True)
    # When user is deleted, their property is also deleted
    landlord_id = models.ForeignKey(User, on_delete = models.CASCADE)
    property_type = models.ForeignKey(PropertyType, null=True, blank=False, on_delete = models.SET_NULL)
    desc= models.CharField(max_length=100, blank=False)
    weekly_price= models.IntegerField(default=0, blank=False)
    address= models.CharField(max_length=30, blank=False)

# Saved Properties by tenant

class SavedProperty(models.Model):
    saved_id = models.BigAutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    saved_on =  models.DateField(auto_now_add=True, blank=False)

# Property Features

class Feature(models.Model):
    feature_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)

class PropertyFeature(models.Model):
    list_id = models.BigAutoField(primary_key=True)
    features_id = models.ForeignKey(Feature, on_delete = models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete = models.CASCADE)

# Property Inspection

class PropertyInspection(models.Model):
    inspection_id = models.BigAutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, blank=False)

class InspectionRegistration(models.Model):
    registration_id = models.BigAutoField(primary_key=True)
    inspection_id = models.ForeignKey(PropertyInspection, on_delete = models.CASCADE)
    inspector_id = models.ForeignKey(User, on_delete = models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True, blank=True)

# Property Application

class PropertyApplication(models.Model):
    application_id = models.BigAutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.CASCADE)
    candidate_id = models.ForeignKey(User, on_delete = models.CASCADE)
    cover_letter = models.CharField(max_length=100, blank=False)
    preferred_start_date =  models.DateField(auto_now_add=True, blank=False)

# Property Lease

class Contract(models.Model):
    contract_id=models.BigAutoField(primary_key=True)

class PropertyLease(models.Model):
    lease_id = models.BigAutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete = models.CASCADE)
    candidate_id = models.ForeignKey(User, on_delete = models.CASCADE)
    contract_id = models.ForeignKey(Contract, null=True, blank=False, on_delete = models.SET_NULL)
    start_date =  models.DateField(auto_now_add=True, blank=False)
    end_date =  models.DateField(auto_now_add=True, blank=False)

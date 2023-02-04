from django.urls import path

from . import views
from thePerfectLandlord import views as site_views

urlpatterns = [
    path('', site_views.vue_test),
]
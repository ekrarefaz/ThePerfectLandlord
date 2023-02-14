from django.urls import include, path
from rest_framework import routers
from . import views

# CRUD API
router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    
    # Authentication API
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    # App API
    path('properties/', views.PropertiesViewSet.as_view()),
]

# In order to login:
# http://localhost:8000/auth/token/login

# In order to register:
# http://localhost:8000/auth/users/
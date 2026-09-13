from django.urls import path, include
from .views import departments, home

urlpatterns = [ 

    path("", home, name="home"),
    path("departments/", departments, name="departments"),
    
]

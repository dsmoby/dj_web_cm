from django.urls import path
from cm.views import home

urlpatterns = [
    path("", home, name="home"),
]

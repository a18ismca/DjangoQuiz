from django.urls import path
from .views import printOut, print
from . import views

urlpatterns = [
    path("", printOut, name="printOut"),
    path("", print, name="print"),
]

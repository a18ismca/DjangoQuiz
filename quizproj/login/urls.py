from django.urls import path
from .views import printOut

urlpatterns = [
    path("", printOut, name="printOutHW"),
]

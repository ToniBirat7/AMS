from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Display_Calendar, name="display-calendar"),
]
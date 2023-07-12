from django.urls import path, include
from . import views
urlpatterns = [
    path('display-calendar/',views.Display_Calendar, name="display-calendar"),
    path('<str:date>/', views.ChooseDate, name="date-choose"),

]
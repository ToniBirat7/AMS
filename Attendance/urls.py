from django.urls import path
from . import views
urlpatterns = [
    path('logged-in/', views.logged_In, name="logged_in"),
    path('profile/', views.Profile, name="profile"),
    path('edit-profile/', views.EditProfile, name="edit-profile"),
    path('image-delete/', views.ImageDelete, name="image-delete"),
  
]

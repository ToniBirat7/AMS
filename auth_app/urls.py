from django.urls import path
from . import views
urlpatterns = [
   path('login/', views.Login , name="login" ),
   path('loginsuccess/', views.Login_Complete , name="register" ),
]
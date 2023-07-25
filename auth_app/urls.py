from django.urls import path
from . import views
urlpatterns = [
   path('login/', views.Login , name="login" ),
   path('logout/', views.Logout , name="logout" ),
   path('forgot/', views.Forgotpswd , name="forgot" ),
   path('', views.UserRegistration, name="user-reg"),
   path('add-person/', views.PersonRegistration, name="person-reg"),
   path('admin-page/', views.AdminPage, name="admin-page"),
   path('add-course/', views.AddCourse, name="add-course"),
   path('add-student/', views.AddStudent, name="add-students"),
   path('add-class/', views.AddClass, name="add-students-class"),

]
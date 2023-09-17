from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('login', views.signup, name='signup'),
    path('substudent', views.substudent, name='substudent'),
    path('insertStudent', views.insertStudent, name='insertStudent')
]
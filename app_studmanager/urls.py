from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('login', views.signup, name='signup'),
    path('substudent', views.substudent, name='substudent'),
    path('insertStudent', views.insertStudent, name='insertStudent'),
    path('gerarcsv', views.gerarcsv, name='gerarcsv'),
    path('update/<int:idAluno>', views.update, name='update'),
    path('uprec/<int:idAluno>', views.uprec, name='uprec'),
    path('delete/<int:idAluno>', views.delete, name="delete"),
]
from django.shortcuts import render
from .models import Aluno
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'login.html')

def substudent(request):
    return render(request, 'substudent.html')

def insertStudent(request):
    if request.method == 'POST':

        ra_aluno = ""

        for i in range(1, 3):
            ra_aluno  += random.choice(letters)

        for i in range(1, 5):
            ra_aluno  += random.choice(numbers)

        nome = request.POST['nome_aluno']
        ra = ra_aluno.upper() 
        email = request.POST['email_aluno']
        nasc = request.POST['nasc_aluno'].replace("/", "-")
        tel = request.POST['tel_aluno']
        turma = request.POST['turma_aluno']

        new_student = Aluno(raAluno = ra, nomeAluno = nome, emailAluno = email, nascAluno = nasc, telAluno = tel, turmaAluno = turma)
        new_student.save()

        students = {
            'students': Aluno.objects.all()
        }

    return render(request, 'substudent.html')
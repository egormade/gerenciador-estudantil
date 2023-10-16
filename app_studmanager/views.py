from django.shortcuts import render, redirect
from .models import Aluno
import pandas as pd
from datetime import date
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'login.html')

def substudent(request):
    alunos = {
            'alunos': Aluno.objects.all().order_by('-idAluno').values()
        }
    
    return render(request, 'substudent.html', alunos)

def teste(request):
    return render(request, 'teste.html')

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
        
        alunos = {
             'alunos': Aluno.objects.order_by('-idAluno').values()
        }
        
    return render(request, 'substudent.html', alunos)

def update(request, idAluno):

    aluno = Aluno.objects.get(idAluno=idAluno)
    return render(request, 'update.html', {'aluno':aluno})

def uprec(request, idAluno):
    nomeAluno = request.POST['nomeAluno']
    emailAluno = request.POST['emailAluno']
    nascAluno = request.POST['nascAluno']
    telAluno = request.POST['telAluno']
    turmaAluno = request.POST['turmaAluno']
    
    aluno = Aluno.objects.get(idAluno=idAluno)

    aluno.nomeAluno = nomeAluno
    aluno.emailAluno = emailAluno
    aluno.nascAluno = nascAluno
    aluno.telAluno = telAluno
    aluno.turmaAluno = turmaAluno

    aluno.save()
    return redirect("/substudent.html")


def delete(request, idAluno):

    alunos = {
             'alunos': Aluno.objects.order_by('-idAluno').values()
        }

    aluno = Aluno.objects.get(idAluno=idAluno)
    aluno.delete()
    return render(request, 'substudent.html', alunos)

def gerarcsv(request):

    alunos = {
            'alunos': Aluno.objects.all()
        }

    hoje = today = date.today()

    data1 = Aluno.objects.all()
    data2 = data1.values()
    # print(data2)
    data2 = pd.DataFrame(data2)
    data2.to_excel(f"alunoscadastrados_{hoje}.xlsx", index=False)
    return render(request, 'substudent.html', alunos)
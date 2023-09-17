from django.db import models

# Create your models here.
class Aluno(models.Model):
    # idAluno = models.AutoField(primary_key=True)
    raAluno = models.CharField(max_length=6)
    nomeAluno = models.CharField(max_length=100)
    emailAluno = models.CharField(max_length=100, default='DEFAULT VALUE')
    nascAluno = models.DateField(default='0000-00-00')
    telAluno = models.IntegerField()
    turmaAluno = models.CharField(max_length=5)

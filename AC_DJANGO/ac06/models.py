from django.db import models

# Create your models here.

class Usuarios(models.Model):

	login = models.CharField("login", max_length = 20)
	senha = models.CharField("Senha", max_length = 15)
	email = models.EmailField("Email", max_length  = 70)
	
	def _str_(self):
		return self.loguin
		


		
class Aluno(models.Model):

	nome = models.CharField("nome", max_length = 50)
	turma = models.CharField("turma", max_length = 5)
	matricula = models.CharField("matricula",unique = True,max_length = 15)

	def _str_(self):
		return self.nome
	
class Professor(models.Model):

	nome = models.CharField("nome", max_length=50)
	Registro = models.CharField("registro",unique = True,max_length = 15)
	celular = models.CharField("celular",max_length=11)
	
	def _str_(self):
		return self.nome
	
class Disciplina (models.Model):

	nome = models.CharField("nome", max_length=50)
	etiqueta = models.SlugField("etiqueta", max_length=50)
	carga_horaria = models.IntegerField("Carga horaria")
	
	def _str_(self):
		return self.nome3
	

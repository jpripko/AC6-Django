from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Aula Django")

# Create your views here.

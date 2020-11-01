from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request) :
	return render(request,'generator/home.html') 

def password(request):

	thepassword = ''

	characters=list('abcdefghijklmnopqrtuvwxyz')

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('specials'):
		characters.extend(list('!@#$%&()[]'))

	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))


	length = int(request.GET.get('length',8))

	for x in range(length) :
		thepassword+=random.choice(characters)

	return render(request,'generator/password.html',{'password': thepassword})	

def About(request) :
	return render(request,'generator/About.html')
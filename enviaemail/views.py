from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def envia_email(request):
    send_mail('Assunto', 'Esse é o e-mail que estou te enviando','avelinogabrieldossantos@gmail.com', ['aluno103.23187221gabriel@gmail.com'])
    return HttpResponse('Olá')

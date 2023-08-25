from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def envia_email(request):
    # send_mail('Assunto', 'Esse é o e-mail que estou te enviando','<remetente>', ['<destinatários>'])

    html_content = render_to_string('emails/cadastro_confirmado.html', {'nome': 'Gabriel'})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives('Cadastro Confirmado', text_content,settings.EMAIL_HOST_USER, ['<destinatários>'])
    email.attach_alternative(html_content, 'text/html')
    email.send()
    return HttpResponse('Olá')

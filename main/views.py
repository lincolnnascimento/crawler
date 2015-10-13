from django.http import HttpResponse
from django.shortcuts import render

import re
import requests
from bs4 import BeautifulSoup

from main.models import *

def index(request):
    dictionary = {}
    if(request.session.get('logado', False) == True):
        template = 'index.html'
    else:
        template = 'login.html'

    return render(request, template, dictionary)

def crawler(request):
    
    for site in Site.objects.all():
        count = 0
        page = requests.get(site.url)
        page = page.text
        soup = BeautifulSoup(page, 'html.parser')

        links = soup.find_all('a')
        
        for link in links:
            link = link.get('href','#')
            if len(link) > 8:
                if link[:7] == 'http://' or link[:8] == 'https://':
                    if Link.objects.filter(url=link).count() == 0:
                        model_link = Link()
                        model_link.site = site
                        model_link.url = link
                        model_link.save()

                        conteudo = requests.get(link).text
                        conteudo = BeautifulSoup(conteudo, "html.parser")

                        for keyword in Keyword.objects.all():
                            reKeyword = re.compile(r'(?ism)\b%s\b'%keyword.name)
                            if reKeyword.search(conteudo.get_text()):
                                if Alerta.objects.filter(url=link).count() == 0:
                                    alerta = Alerta()
                                    alerta.site = site
                                    alerta.url = link
                                    alerta.texto = conteudo
                                    alerta.save()
                                    alerta.palavras_chave.add(keyword)
                                    try:
                                        alerta.save()
                                    except:
                                        #TODO 
                                        #Exception Value: 'NoneType' object is not callable
                                        pass
                                    count = count + 1;
                                else:
                                    alerta = Alerta.objects.filter(url=link)[0]
                                    alerta.palavras_chave.add(keyword)
                                    alerta.save()

    response = str(count) + ' alertas cadastrados com as palavras chaves designadas.'
    return HttpResponse(response)
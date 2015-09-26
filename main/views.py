from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup

from main.models import *

def index(request):
    for site in Site.objects.all():
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
                        conteudo = BeautifulSoup(conteudo)

                        if conteudo.get_text().find('amor') != -1:
                            alerta = Alerta()
                            alerta.site = site
                            alerta.url = link
                            alerta.texto = conteudo
                            alerta.palavras_chave = 'amor'
                            alerta.save()

    return HttpResponse('Nothing here...')
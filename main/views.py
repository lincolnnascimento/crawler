from django.http import HttpResponse
import re
import requests
from bs4 import BeautifulSoup

from main.models import *

def index(request):
    reKeyword = re.compile(r'(?ism)\bamor\b')
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
                        conteudo = BeautifulSoup(conteudo, "html.parser")
                        if reKeyword.search(conteudo.get_text()):
                            alerta = Alerta()
                            alerta.site = site
                            alerta.url = link
                            alerta.texto = conteudo
                            alerta.palavras_chave = 'amor'
                            alerta.save()

    return HttpResponse('<h2>Crawled!</h2>')
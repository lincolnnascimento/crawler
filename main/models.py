from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=150)

    def __unicode__(self):
        return self.name

class Link(models.Model):
    site = models.ForeignKey(Site)
    url = models.URLField(max_length=150)

    def __unicode__(self):
        return self.url

class Alerta(models.Model):
    site = models.ForeignKey(Site)
    url = models.URLField(max_length=150)
    texto = models.TextField()
    palavras_chave = models.ManyToManyField(Keyword)
    data_encontro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.url
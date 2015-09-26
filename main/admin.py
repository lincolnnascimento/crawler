from django.contrib import admin
from main.models import Site, Link, Alerta

admin.site.register(Site)
admin.site.register(Link)

class AlertaAdmin(admin.ModelAdmin):
    list_display = ('site', 'url', 'palavras_chave')

admin.site.register(Alerta, AlertaAdmin)
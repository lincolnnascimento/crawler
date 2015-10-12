from django.contrib import admin
from main.models import Site, Link, Alerta, Keyword

admin.site.register(Site)
admin.site.register(Link)
admin.site.register(Keyword)

class AlertaAdmin(admin.ModelAdmin):
    list_display = ('site', 'url')

admin.site.register(Alerta, AlertaAdmin)
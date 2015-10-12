from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.index', name='index'),
    url(r'^crawler/', 'main.views.crawler', name='crawler'),
    url(r'^admin/', include(admin.site.urls)),
)

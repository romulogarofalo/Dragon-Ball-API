from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','sagas.views.index'),
    url(r'^type_character/$','character.views.get_all_types'),
    url(r'^type_character/(?P<type_character_id>\d+)/','character.views.get_type'),
    url(r'^characters/$','character.views.get_characters'),
    url(r'^sagas/$','sagas.views.get_all_sagas'),
    url(r'^sagas/inserir$','sagas.views.inserir_saga')
)

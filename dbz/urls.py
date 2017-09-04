from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$','sagas.views.index'),
    url(r'^type_character/$','character.views.get_all_types'),
    url(r'^type_character/(?P<type_character_id>\d+)/','character.views.get_type'),
    url(r'^characters/$','character.views.get_characters'),
    url(r'^characters/(?P<name_or_id>\d+)/','character.views.get_character'),
    url(r'^sagas/$','sagas.views.get_all_sagas'),
    url(r'^sagas/(?P<id_saga>\d+)/','sagas.views.get_saga'),
    url(r'^fusion/$','fusion.views.get_all_fusions'),
    url(r'^fusion/(?P<name_or_id>\d+)','fusion.views.get_fusion')
)

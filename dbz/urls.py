from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','sagas.views.index'),
    url(r'^type_character/','character.views.get_all_types')
)

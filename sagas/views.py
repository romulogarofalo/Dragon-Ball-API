from django.shortcuts import render
from django.http import HttpResponse
from sagas.models import saga
from character.models import character
import json

# Create your views here.


def index(request):

    data = {'foo': 'bar', 'hello': 'world'}
    return HttpResponse(json.dumps(data), content_type='application/json')

def get_all_sagas(request):
    allsagas = saga.objects.all()
    sagas = []
    for temp in allsagas:
        sag = {}
        sag["id"] = temp.id
        sag["nm_saga"] = temp.nm_saga
        sag["ds_saga"] = temp.ds_saga
        sag["img_saga"] = temp.img_saga
        sagas.append(sag)
    return HttpResponse(json.dumps(sagas), content_type='application/json')

def get_saga(request, id_saga):
    historia = saga.objects.get(id=int(id_saga))
    personagens = character.objects.get(saga_id=int(id_saga))
    sag = {}
    allcharacter = []
    for carinhas in personagens:
        pers= {}
        pers["nm_character"] = personagens.nm_character
        pers["id"] = personagens.id
        allcharacter.append(pers)
    sag["id"] = historia.id
    sag["nm_saga"] = historia.nm_saga
    sag["characters"] = allcharacter
    sag["ds_saga"] = historia.ds_saga
    sag["img_saga"] = historia.img_saga
    return HttpResponse(json.dumps(sag), content_type='application/json')
from django.shortcuts import render
from character.models import character
from character.models import type_character
from saga.models import saga
from django.http import HttpResponse
import json

# Create your views here.
def get_all_types(request):
    alltypes = type_character.objects.all()
    races = []
    for tipo in alltypes:
        race = {}
        race["id"] = tipo.id
        race["race"] = tipo.nm_type_character
        races.append(race)
        
    return HttpResponse(json.dumps(races), content_type='application/json')

def get_type(request, type_character_id):
    tipo = type_character.objects.get(id=int(type_character_id))
    race = {}
    race["id"]=tipo.id
    race["nm_type_character"]= tipo.nm_type_character
    
    return HttpResponse(json.dumps(race), content_type='application/json')
    
def get_characters(request):
    allcharacters = character.objects.all()
    personagens = []
    for chares in allcharacters:
        charc = {}
        charc["id"] = chares.id
        charc["nm_character"] = chares.nm_character
        charc["img_character"]= chares.img_character
        charc["fighting_power"]= chares.fighting_power
        charc["race"]= type_character.objects.get(id=int(chares.type_id)).nm_type_character
        charc["saga"]= saga.objects.get(id=int(chares.saga_id)).nm_saga
        personagens.append(charc)
    return HttpResponse(json.dumps(personagens), content_type='application/json')

def get_character(request,name_or_id):
    result = {}
    if name_or_id.isnumeric():
        allcharacters = character.objects.get(id=int(name_or_id))
        result["id"] = allcharacters.id
        result["nm_character"] = allcharacters.nm_character
        result["img_character"] = allcharacters.img_character
        result["fighting_power"] = allcharacters.fighting_power
        result["race"] = type_character.objects.get(id=int(allcharacters.type_id)).nm_type_character
        result["saga"] = saga.objects.get(id=int(allcharacters.saga_id)).nm_saga
    else:
        alllike = []
        allcharacters = character.objects.filter(string__contains=name_or_id)
        for chares in allcharacters:
            charc = {}
            charc["id"] = chares.id
            charc["nm_character"] = chares.nm_character
            charc["img_character"]= chares.img_character
            charc["fighting_power"]= chares.fighting_power
            charc["race"]= type_character.objects.get(id=int(chares.type_id)).nm_type_character
            charc["saga"]= saga.objects.get(id=int(chares.saga_id)).nm_saga
            alllike.append(chares)
        result["characters"] = alllike
    return HttpResponse(json.dumps(result), content_type='application/json')
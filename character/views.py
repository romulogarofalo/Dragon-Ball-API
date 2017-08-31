from django.shortcuts import render
from character.models import type_character
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

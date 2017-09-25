from django.shortcuts import render
from django.http import HttpResponse
from character.models import character
from fusion.models import fusion
from fusion.models import type_fusion
import json

def get_all_fusions(request):
    allfusoes = fusion.objects.all()
    fusoes = []
    for fusao in allfusoes:
        fug = {}
        fug["id"] = fusao.id
        fug["nm_character_fusion"] = fusao.nm_character_fusion
        fug["character1_id"] = fusao.character1_id.id
        fug["character2_id"] = fusao.character2_id.id
        fug["nm_type_fusion"] = fusao.type_fusion_id.nm_type_fusion
        fusoes.append(fug)
    return HttpResponse(json.dumps(fusoes), content_type='application/json')
    
def get_fusion(request,name_or_id):
    result = {}
    if name_or_id.isnumeric():
        all_fusions = fusion.objects.get(id=int(name_or_id))
        result["id"] = all_fusions.id
        result["nm_character_fusion"] = all_fusions.nm_character_fusion
        result["character1_id"] = all_fusions.character1_id.id
        result["character2_id"] = all_fusions.character2_id.id
        result["nm_type_fusion"] = all_fusions.type_fusion_id.nm_type_fusion
    else:
        alllike = []
        allfusions = fusion.objects.filter(string__contains=name_or_id)
        for fusao in allfusions:
            fus = {}
            fus["id"] = fusao.id
            fus["nm_character_fusion"] = fusao.nm_character_fusion
            fus["character1_id"] = fusion.character1_id
            fus["character2_id"] = fusion.character2_id
            fus["nm_type_fusion"] = fusion.type_fusion_id.nm_type_fusion
            alllike.append(fus)
        result["fusions"] = alllike
    return HttpResponse(json.dumps(result), content_type='application/json')
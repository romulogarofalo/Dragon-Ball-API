from django.shortcuts import render
from character.models import character
from character.models import type_character
from sagas.models import saga
from fusion.models import type_fusion
from fusion.models import fusion
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
    
def seeds(request):
    sg = saga(nm_saga="Dragon Ball",ds_saga="Dragon Ball é o anime que deu inicio a saga de Son Goku e a procura pelas esferas do dragão que quando unidas invoca o grande dragão Shenlong que realizará quaisquer desejo. Goku juntamente com seus amigos Mestre Kame, Kuririn, Bulma, Yancha vão viver grandes aventuras desde a batalha contra a terrível organização Red Ribbon e o seu mortal assassino Tao-Pai-Pai, passando pelo grande torneio de artes marciais lutando contra Tenchin-han e Kaos e acabando com a saga de Piccollo e sua tentativa de destruir a Terra",img_saga="https://i.pinimg.com/originals/77/82/f0/7782f08f34d373c4caf42aee9160a32d.jpg")
    sg.save()
    sg = saga(nm_saga="Dragon Ball Z",ds_saga="Depois da batalha contra Piccollo Dai-Maoh goku se casa com a Princesa Chichi e tem um filho chamado Gohan e vivem em paz na floresta até a chegada dos temíveis Sayajins que vêem do espaço a procura de Goku. Nesta Saga Son-Goku descobre sua verdadeira origem sayajin combatendo o impiedoso Vegeta e ainda em Dragon Ball Z vai viver incriveis lutas contra o temível Freeza no Planeta Namek, contra o super andróide Cell em seu torneio de artes marciais acabando na batalha contra o monstro Boo. Assista Dragon Ball Z e conheça o verdadeiro poder do Lendário Super Sayajin e suas evoluções!",img_saga="http://ptanime.com/wp-content/uploads/2015/05/Dragon_Ball_Z_Analise_Imagem_Saga_Majin_Buu.jpg")
    sg.save()
    sg = saga(nm_saga="Dragon Ball GT",ds_saga="Este anime se passa 10 anos depois da saga de Dragon Ball Z e esta focado em 3 personagens principais: Son Goku, sua neta Pan e o Jovem Trunks.Graças ao pedido filho de Pilaf (inimigo de Goku em Dragon Ball) que recolhe as dragon balls, Goku se torna novamente criança mas as dragon balls perdem seu poder e com isso a Terra corre perigo pois as esferas do dragão estão intimamente ligadas ao planeta, assim Goku, Pan e Trunks saem a procura das blacks dragon ball no espaço para ressucitarem as esferas do dragão da Terra, será que chegarão a tempo de salvar a Terra? Enquanto Goku esta fora , Bebi o tsufurujin está dominando a mente dos terráqueos e também da Familia de Goku: Chichi, Gohan e Goten, esta é uma empolgante aventura onde poderemos ver a luta de goku contra os terriveis dragões e também o poder máximo dos sayajin, o super sayajin 4.",img_saga="https://vignette2.wikia.nocookie.net/dbz-dokkanbattle/images/9/95/Black_Star_DB_Saga.png/revision/latest?cb=20160910202651")
    sg.save()
    sg = saga(nm_saga="Dragon Ball Super",ds_saga="a continuação de Dragon Ball Z e agora com Lorde Bils a procura do deus super sayajin",img_saga="https://i.pinimg.com/originals/81/57/19/81571933f0d137e2d6c98304e0376311.png")
    sg.save()
    tpf = type_fusion(nm_type_fusion="Potara Fusion")
    tpf.save()
    tpf2 = type_fusion(nm_type_fusion="Fusion Dance")
    tpf2.save()
    tpp = type_character(nm_type_character="Human")
    tpp.save()
    tpp = type_character(nm_type_character="Sayajin")
    tpp.save()
    tpp = type_character(nm_type_character="Namekuseijin")
    tpp.save()
    tpp = type_character(nm_type_character="Androide")
    tpp.save()
    tpp = type_character(nm_type_character="Majin")
    tpp.save()
    p = character(nm_character="Goku",img_character="http://www.imagenswiki.com/Uploads/imagenswiki.com/ImagensGrandes/son-goku-crianca.jpg",fighting_power="260",type_id=2,saga_id=1)
    p.save()
    p = character(nm_character="Goku",img_character="https://vignette.wikia.nocookie.net/dragonball/images/5/5b/Gokusteppingoutofaspaceship.jpg/revision/latest/scale-to-width-down/224?cb=20150325220848",fighting_power="924",type_id=2,saga_id=2)
    p.save()
    p = character(nm_character="Goku Super Sayajin 1",img_character="https://dreager1.files.wordpress.com/2011/08/snap2149516qs7.jpg",fighting_power="150000000",type_id=2,saga_id=2)
    p.save()
    p = character(nm_character="Goku Super Sayajin 2",img_character="https://vignette.wikia.nocookie.net/dragonball/images/a/ac/Goku-Super-Saiyan-2-.jpg/revision/latest?cb=20110426171840",fighting_power="6000000000",type_id=2,saga_id=2)
    p.save()
    p = character(nm_character="Goku Super Sayajin 3",img_character="https://vignette2.wikia.nocookie.net/dragonuniverse/images/8/89/SSJ3.png/revision/latest?cb=20160928233848",fighting_power="10000000000",type_id=2,saga_id=2)
    p.save()
    p = character(nm_character="Goku",img_character="https://vignette.wikia.nocookie.net/dragonball/images/5/5b/Gokusteppingoutofaspaceship.jpg/revision/latest/scale-to-width-down/224?cb=20150325220848",fighting_power="924",type_id=2,saga_id=4)
    p.save()
    p = character(nm_character="Goku Super Sayajin 1",img_character="https://dreager1.files.wordpress.com/2011/08/snap2149516qs7.jpg",fighting_power="150000000",type_id=2,saga_id=4)
    p.save()
    p = character(nm_character="Goku Super Sayajin 2",img_character="https://vignette.wikia.nocookie.net/dragonball/images/a/ac/Goku-Super-Saiyan-2-.jpg/revision/latest?cb=20110426171840",fighting_power="6000000000",type_id=2,saga_id=4)
    p.save()
    p = character(nm_character="Goku Super Sayajin 3",img_character="https://vignette2.wikia.nocookie.net/dragonuniverse/images/8/89/SSJ3.png/revision/latest?cb=20160928233848",fighting_power="10000000000",type_id=2,saga_id=4)
    p.save()
    p = character(nm_character="Goku Super Sayajin Blue",img_character="http://vignette1.wikia.nocookie.net/dragonball/images/1/12/SSGSS_GOKU.png/revision/latest?cb=20151025084338",fighting_power="100000000000",type_id=2,saga_id=4)
    p.save()
    p = character(nm_character="Little Goku",img_character="https://i.stack.imgur.com/6HrTE.jpg",fighting_power="10000000",type_id=2,saga_id=3)
    p.save()
    p = character(nm_character="Little Goku Super Saiyan 1",img_character="https://static.comicvine.com/uploads/original/14/149746/3647183-4101411823-Goku_.jpg",fighting_power="150000000",type_id=2,saga_id=3)
    p.save()
    p = character(nm_character="Little Goku Super Sayajin 2",img_character="http://vignette2.wikia.nocookie.net/dragonball/images/7/7f/GT_Kid_Goku_Super_Saiyan_2_by_dbzataricommunity.jpg/revision/latest?cb=20110412181525",fighting_power="6000000000",type_id=2,saga_id=3)
    p.save()
    p = character(nm_character="Little Goku Super Sayajin 3",img_character="http://pm1.narvii.com/6152/0abf4a01f38c1f84e7ea32e9601aaa1575b93e7e_hq.jpg",fighting_power="10000000000",type_id=2,saga_id=3)
    p.save()
    p = character(nm_character="Goku Super Sayajin 4",img_character="http://vignette4.wikia.nocookie.net/p__/images/f/f1/Goku_Super_Saiyan_4.png/revision/latest?cb=20130805024507&path-prefix=protagonist",fighting_power="100000000000",type_id=2,saga_id=3)
    p.save()
    
    tp = fusion(type_fusion_id=1,character1_id=1,character2_id=2,nm_character_fusion="Vegetto")
    tp.save()
    tpf2.save()
    tp2 = fusion(type_fusion_id=2,character1_id=1,character2_id=2,nm_character_fusion="Gojeta")
    tp2.save()
    
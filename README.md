![logo_prj](https://github.com/Bolinhozz/dbz_api/blob/master/dbz_api.png)

<table>
    <tr>
        <td>
        <sub>
       	 	<h2>
			This project is about things that are special to me. It entails:</br></br>
1. My favorite anime - Dragon Ball;</br>
2. While using my preferred programming language - <a href="https://www.python.org/">Python</a> with a <a href="https://www.djangoproject.com/">Django</a> framwork. </br></br>
The purpose of this initiative is to provide an API REST that will allow users to get all kinds of information about the anime. Enjoy!
       	 	</h2>
        </sub>
        </td>
    </tr>
</table>

| Routes                                        | Description                                    | Methods HTTP     |
|-----------------------------------------------|------------------------------------------------|------------------|
| /sagas                                        | return the informations of all sagas           | GET              |
| /sagas/#id                                    | return the informations of a specific saga     | GET              |
| /fusion                                       | return all fuions of the anime                 | GET              |
| /fusion/#id                                   | return the informations of a specific fuions   | GET              |
| /characters                                   | return all character of the anime              | GET              |
| /characters/#nameOrId                         | return the informations of a specific character| GET              |
| /type_character                               | return all races of the anime                  | GET              |
| /type_character/#id                           | return the informations of a specific race     | GET              |
| /seeds                                        | seed all the informations about the anime      | GET(shoud be a POST)|


## SAGA
#### /saga
	[{
		"nm_saga": "Dragon Ball",
		"img_saga": "https://i.pinimg.com/originals/77/82/f0/7782f08f34d373c4caf42aee9160a32d.jpg",
		"id": 1,
		"ds_saga": "Dragon Ball \u00e9 o anime que deu inicio a saga de Son Goku e a procura pelas esferas do dragao que quando unidas invoca o grande dragao Shenlong que realizara quaisquer desejo. Goku juntamente com seus amigos Mestre Kame, Kuririn, Bulma, Yancha vao viver grandes aventuras desde a batalha contra a terrivel organiza\u00e7\u00e3o Red Ribbon e o seu mortal assassino Tao-Pai-Pai, passando pelo grande torneio de artes marciais lutando contra Tenchin-han e Kaos e acabando com a saga de Piccollo e sua tentativa de destruir a Terra"
	}, {
		"nm_saga": "Dragon Ball Z",
		"img_saga": "http://ptanime.com/wp-content/uploads/2015/05/Dragon_Ball_Z_Analise_Imagem_Saga_Majin_Buu.jpg",
		"id": 2,
		"ds_saga": "Depois da batalha contra Piccollo Dai-Maoh goku se casa com a Princesa Chichi e tem um filho chamado Gohan e vivem em paz na floresta at\u00e9 a chegada dos tem\u00edveis Sayajins que v\u00eaem do espa\u00e7o a procura de Goku. Nesta Saga Son-Goku descobre sua verdadeira origem sayajin combatendo o impiedoso Vegeta e ainda em Dragon Ball Z vai viver incriveis lutas contra o tem\u00edvel Freeza no Planeta Namek, contra o super andr\u00f3ide Cell em seu torneio de artes marciais acabando na batalha contra o monstro Boo. Assista Dragon Ball Z e conhe\u00e7a o verdadeiro poder do Lend\u00e1rio Super Sayajin e suas evolu\u00e7\u00f5es!"
	}, {
		"nm_saga": "Dragon Ball GT",
		"img_saga": "https://vignette2.wikia.nocookie.net/dbz-dokkanbattle/images/9/95/Black_Star_DB_Saga.png/revision/latest?cb=20160910202651",
		"id": 3,
		"ds_saga": "Este anime se passa 10 anos depois da saga de Dragon Ball Z e esta focado em 3 personagens principais: Son Goku, sua neta Pan e o Jovem Trunks.Gra\u00e7as ao pedido filho de Pilaf (inimigo de Goku em Dragon Ball) que recolhe as dragon balls, Goku se torna novamente crian\u00e7a mas as dragon balls perdem seu poder e com isso a Terra corre perigo pois as esferas do drag\u00e3o est\u00e3o intimamente ligadas ao planeta, assim Goku, Pan e Trunks saem a procura das blacks dragon ball no espa\u00e7o para ressucitarem as esferas do drag\u00e3o da Terra, ser\u00e1 que chegar\u00e3o a tempo de salvar a Terra? Enquanto Goku esta fora , Bebi o tsufurujin est\u00e1 dominando a mente dos terr\u00e1queos e tamb\u00e9m da Familia de Goku: Chichi, Gohan e Goten, esta \u00e9 uma empolgante aventura onde poderemos ver a luta de goku contra os terriveis drag\u00f5es e tamb\u00e9m o poder m\u00e1ximo dos sayajin, o super sayajin 4."
	}, {
		"nm_saga": "Dragon Ball Super",
		"img_saga": "https://i.pinimg.com/originals/81/57/19/81571933f0d137e2d6c98304e0376311.png",
		"id": 4,
		"ds_saga": "a continua\u00e7\u00e3o de Dragon Ball Z e agora com Lorde Bils a procura do deus super sayajin"
	}]

## Instructions to install
### if you use Linux
#### Frist you going need pip 
	sudo apt-get install python-pip
---------------------------------------------------------------------------
#### Now you can install the framework Django
	sudo pip install django==1.7.4
---------------------------------------------------------------------------
#### Clone the project
	git clone https://github.com/Bolinhozz/dbz_api.git
---------------------------------------------------------------------------
#### Generating the database schema
	python manage.py makemigrations
---------------------------------------------------------------------------
#### Create the database with the schema
	python manage.py migrate
---------------------------------------------------------------------------
#### Start the server
	python manage.py runserver
---------------------------------------------------------------------------
#### Finaly use the route seeds and its ready to use
	localhost:8000/seeds
---------------------------------------------------------------------------
### If you use Windows
	install Ubuntu

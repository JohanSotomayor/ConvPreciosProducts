def run ():
    pass

lista_productos =["""Ace combat 70 
Anthem 60 
Asassins ezio 70 
Asassins odisey 85 
Asassins origins 75
Assasins sindicate $ 70 
Assassins unity 60 
Assassins valhala $ 170 
Avengers $ 140 
Batman arkham night 70
Batman return to arkham $70 
Battelfield 1 55 
Battelfield 4 55 
Battelfield 5 75 
Bioshock collection 70 
Bloodborne 60 
Borderlands 3 95 
Caballeros del zodiaco 70
Call of dutty cold war 190
Call of dutty legacy 65 
Call of dutty black ops 4 Ingles 75
Call of dutty black ops4 español  90
Capitan tsubasa 110 
Cars 3 70
Crash Kart $ 115 
Crash 4 155 
Darksouls edición completa 75 
Days Gone 90 
Dead stranding 100 
Detroit becom human 65 
Devil my cry 5 85
Dirt rally 2.0 día 1 $ 75 
División 2 90 
Doom anterior 70
Dragón ball xenoverse 2 70 
Dragon fighterz 75 
Dragón ball kakaroto $ 125 
Driverclub 55 
Fallout 4 $ 60 
Fallout 76 edición completa 65 
Farcry 4 60 
Farcry primal 70 
Fifa 21 100
Final fantasy tipo 0 $ 40
Fornite the last laugh 115 
Ghost of tsushima $ 165 
God of war 3 60 
God of war 4 65 
Gran turismo 65 
Ghost recon Wilands 75 
Ghost recon breakpoint 120 
Ghost recon breackpoint Edición completa 130
Gta 5 $ 75 
Horizont edición completa 70 
Infamous second 60
Injustice legendario 80 
Jump force 80
Just cause 4 75 
Just dance 20 105 
Just dance 21 145 
Killzone 65 
Kimdom hearts 3 75 
Lego avengers 65 
Lego movie 2 70
Lego marvel coll 90 
Lego city 65 
lego harry potter 70 
Lego increíbles 75 
Lego jurassic 70 
Lego star wars 65 
Little big planet 60 
Madden 21 $ 110 
Mafia 3 70 
Metal gear definitivo 80 
Minecraft dungeon $ 105 
Minecraft normal 115 
Monster hunter world 75 
Mortal kombat XL $ 70 
Moto gp 20 $ 120
Naruto boruto 4 $ 80 
Nba 21 $ 140 
Nfs azul 65 
Nfs hot porsuit $ 125 
Nfs payback $ 70 
Nfs revals 65 
Nier replicant 175 
Nioh 65 
Nioh 2 140 
Persona 5 75 
Pes 17 20
Pes 21 85 
Plantas vs zombies 3 85 
Puyo puyo 50
Project cars edición normal 60
Project cars 2 70 
Project cars 3 $ 135 
Raiman 60 
Ratchet 60 
Raimbow six 65 
Rayman 60 
Red dead redemption 120 
Resident 2 90 
Resident 3 110 
Resident 6 70
Resident origins 65 
Resident 8 $ 175 
Resident 8 deluxe $ 220 
Ride 2 65 
Sekiro $ 140 
Sims 4 $ 80 
Shadow colossus 65 
Shadow war edición completa 90 
Sniper elite 3 60
Sniper elite 4 80
Sonic racing 110 
Sonic mania 100 
Spiderman GOTY 100 
Spiderman morales $ 160
Spyro 80
Star wars battelfront 2 $ 65 
Street fighters 5 65 
Street fighter 30 años 80 
Soulcalibur 6 55 
Tekken 7 65 
The crew 1 60
The crew 2 105 
The last of Us 65 
The last of us 2 125 
The witcher edición completa 100 
Titán fall 2 55 
Tomb raider shadow 80 
Tomb raider 20 años $ 80 
Ufc 4 $ 135 
Uncharted collection 65 
Uncharted legacy 65 
Untildown 65 
Valentino rossi 65 """]





if __name__ =='__main__':
    # print({lista_productos[0]})
    lista_productos[0]=lista_productos[0].replace(" \n", '", "')
    lista_productos[0]=lista_productos[0].replace("\n", '", "')
    lista_productos[0]=lista_productos[0].replace("$", "")
    print({lista_productos[0]})
    lista_productos1 =["Ace combat 70", "Anthem 60", "Asassins ezio 70", "Asassins odisey 85", "Asassins origins 75", "Assasins sindicate  70", "Assassins unity 60", "Assassins valhala  170", "Avengers  140", "Batman arkham night 70", "Batman return to arkham 70", "Battelfield 1 55", "Battelfield 4 55", "Battelfield 5 75", "Bioshock collection 70", "Bloodborne 60", "Borderlands 3 95", "Caballeros del zodiaco 70", "Call of dutty cold war 190", "Call of dutty legacy 65", "Call of dutty black ops 4 Ingles 75", "Call of dutty black ops4 español  90", "Capitan tsubasa 110", "Cars 3 70", "Crash Kart  115", "Crash 4 155", "Darksouls edición completa 75", "Days Gone 90", "Dead stranding 100", "Detroit becom human 65", "Devil my cry 5 85", "Dirt rally 2.0 día 1  75", "División 2 90", "Doom anterior 70", "Dragón ball xenoverse 2 70", "Dragon fighterz 75", "Dragón ball kakaroto  125", "Driverclub 55", "Fallout 4  60", "Fallout 76 edición completa 65", "Farcry 4 60", 
"Farcry primal 70", "Fifa 21 100", "Final fantasy tipo 0  40", "Fornite the last laugh 115", "Ghost of tsushima  165", "God of war 3 60", "God of war 4 65", "Gran turismo 65", "Ghost recon Wilands 75", "Ghost recon breakpoint 120", "Ghost recon breackpoint Edición completa 130", "Gta 5  75", "Horizont edición completa 70", "Infamous second 60", "Injustice legendario 80", "Jump force 80", "Just cause 4 75", "Just dance 20 105", "Just dance 21 145", "Killzone 65", "Kimdom hearts 3 75", "Lego avengers 65", "Lego movie 2 70", "Lego marvel coll 90", "Lego city 65", "lego harry potter 70", "Lego increíbles 75", "Lego jurassic 70", "Lego star wars 65", "Little big planet 60", "Madden 21  110", "Mafia 3 70", "Metal gear definitivo 80", "Minecraft dungeon  105", "Minecraft normal 115", "Monster hunter world 75", "Mortal kombat XL  70", "Moto gp 20  120", "Naruto boruto 4  80", "Nba 21  140", "Nfs azul 65", "Nfs hot porsuit  125", 
"Nfs payback  70", "Nfs revals 65", "Nier replicant 175", "Nioh 65", "Nioh 2 140", "Persona 5 75", "Pes 17 20", "Pes 21 85", "Plantas vs zombies 3 85", "Puyo puyo 50", "Project cars edición normal 60", "Project cars 2 70", "Project cars 3  135", "Raiman 60", "Ratchet 60", "Raimbow six 65", "Rayman 60", "Red dead redemption 120", "Resident 2 90", "Resident 3 110", "Resident 6 70", "Resident origins 65", "Resident 8  175", "Resident 8 deluxe  220", "Ride 2 65", "Sekiro  140", "Sims 4 80", "Shadow colossus 65", "Shadow war edición completa 90", "Sniper elite 3 60", "Sniper elite 4 80", "Sonic racing 110", "Sonic mania 100", "Spiderman GOTY 100", "Spiderman morales  160", "Spyro 80", "Star wars battelfront 2  65", "Street fighters 5 65", "Street fighter 30 años 80", "Soulcalibur 6 55", "Tekken 7 65", "The crew 1 60", "The crew 2 105", "The last of Us 65", "The last of us 2 125", "The witcher edición completa 100", "Titán fall 2 55", "Tomb raider shadow 80", "Tomb raider 20 años  80", "Ufc 4  135", "Uncharted collection 65", "Uncharted legacy 65", "Untildown 65", "Valentino rossi 65"]

    # for i in range(40,201):
    #     print(i)
    #     e=i+40
    #     print(e)
    #     lista_productos[0]=lista_productos[0].replace(f'{i}",', f'{e}",')
    leng= len(lista_productos1)
    print("-----------------------------------------------------------------------------------------------")
    print(leng)
    for i in range (0, leng):
       
        for j in range(40,201):
             h=str(j)
             e=str(int(j)+40)
             lista_productos1[i]=lista_productos1[i].replace(f' {h}', f' ${e}.000')
             j=0
        
        
    print("-----------------------------------------------------------------------------------------------")
    print(lista_productos1)

    #      lista_productos1[element].slice(-1, -3, -1)
    #      print({lista_productos1[element]})
        #  slice_object = int(slice(-1, -3, -1))
        #  print(lista_productos1[slice_object]) 
#     lista_productos1 = {"Ace combat :70", "Anthem :60", "Asassins ezio :70", "Asassins odisey :85", "Asassins origins :75", "Assasins sindicate  :70", "Assassins unity :60", "Assassins valhala  1:70", "Avengers  1:40", "Batman arkham night :70", "Batman return to arkham :70", "Battelfield 1 :55", "Battelfield 4 :55", "Battelfield 5 :75", "Bioshock collection :70", "Bloodborne :60", "Borderlands 3 :95", "Caballeros del zodiaco :70", "Call of dutty cold war 1:90", "Call of dutty legacy :65", "Call of dutty black ops 4 Ingles :75", "Call of dutty black ops4 español  :90", "Capitan tsubasa :110", "Cars 3 :70", "Crash Kart  :115", "Crash 4 1:55", "Darksouls edición completa :75", "Days Gone :90", "Dead stranding :100", "Detroit becom human :65", "Devil my cry 5 :85", "Dirt rally 2.0 día 1  :75", "División 2 :90", "Doom anterior :70", "Dragón ball xenoverse 2 :70", "Dragon fighterz :75", "Dragón ball kakaroto  :125", "Driverclub :55", "Fallout 4  :60", "Fallout 76 edición completa :65", "Farcry 4 :60", "Farcry primal :70", "Fifa 21 :100", "Final fantasy tipo 0  :40", "Fornite the last laugh :115", "Ghost of tsushima  1:65", "God of war 3 :60", "God of war 4 :65", "Gran turismo :65", "Ghost recon Wilands :75", "Ghost recon breakpoint :120", "Ghost recon breackpoint Edición completa :130", "Gta 5  :75", "Horizont edición completa :70", "Infamous second :60", "Injustice legendario :80", "Jump force :80", "Just cause 4 :75",
#      "Just dance 20 :105", "Just dance 21 1:45", "Killzone :65", "Kimdom hearts 3 :75", "Lego avengers :65", "Lego movie 2 :70", "Lego marvel coll :90", "Lego city :65", "lego harry potter :70", "Lego increíbles :75", "Lego jurassic :70", "Lego star wars :65", "Little big planet :60", "Madden 21  :110", "Mafia 3 :70", "Metal gear definitivo :80", "Minecraft dungeon  :105", "Minecraft normal :115", "Monster hunter world :75", "Mortal kombat XL  :70", "Moto gp 20  :120", "Naruto boruto 4  :80", "Nba 21  1:40",  
# "Nfs azul :65", "Nfs hot porsuit  :125", "Nfs payback  :70", "Nfs revals :65", "Nier replicant 1:75", "Nioh :65", "Nioh 2 1:40", "Persona 5 :75", "Pes 17 20", "Pes 21 :85", "Plantas vs zombies 3 :85", "Puyo puyo :50", "Project cars edición normal :60", "Project cars 2 :70", "Project cars 3  :135", "Raiman :60", "Ratchet :60", "Raimbow six :65", "Rayman :60", "Red dead redemption :120", "Resident 2 :90", "Resident 3 :110", "Resident 6 :70", "Resident origins :65", "Resident 8  1:75", "Resident 8 deluxe  220", "Ride 2 :65", "Sekiro  1:40", "Sims 4  :80", "Shadow colossus :65", "Shadow war edición completa :90", "Sniper elite 3 :60", "Sniper elite 4 :80", "Sonic racing :110", 
# "Sonic mania :100", "Spiderman GOTY :100", "Spiderman morales  1:60", "Spyro 80 3 e1", "Star wars battelfront 2  :65", "Street fighters 5 :65", "Street fighter 30 años :80", "Soulcalibur 6 :55", "Tekken 7 :65", "The crew 1 :60", "The crew 2 :105", "The last of Us :65", "The last of us 2 :125", "The witcher edición completa :100", "Titán fall 2 :55", "Tomb raider shadow :80", "Tomb raider 20 años  :80", "Ufc 4  :135", "Uncharted collection :65", "Uncharted legacy :65", "Untildown :65", "Valentino rossi :65"}
    # lista_productos1 = {
    # 'Ace combat' :70, 
    # 'Anthem' :60, 
    # 'Asassins ezio':70}
    # print("-----------------------------------------------------------------------------------------------")
    # n=lista_productos1.values['Anthem']
    
    # for e in lista_productos1.values():
        # print(lista_productos1.values)
        # lista_productos1.values()=int(e)+40
    

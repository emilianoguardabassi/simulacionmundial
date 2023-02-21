import random

class Football:
    def __init__(self,name,attack,deffend,passing,freekick,playmake):
        self.name=name
        self.attack=attack
        self.deffend=deffend
        self.passing=passing
        self.freekick=freekick
        self.playmake=playmake
        self.grouppoints=0
        self.gf=0
        self.gc=0
        

    def __str__(self):
        return f"{self.name}: AT {self.attack}, DF {self.deffend}, PAS {self.passing}, TL {self.freekick}, SG {self.playmake}"


    def offensive(self):
        dadoattack=random.randint(self.attack,100)
        return dadoattack

    def deffensive(self):
        dadodef=random.randint(self.deffend,100)
        return dadodef

    def playmakechance(self):
        chance=random.randint(self.playmake,100)
        if chance >= 70:
            plays=(chance-70)//3
        return plays

    def fkgoalchance(self):
        chance=random.randint(self.freekick,100)
        if chance>99:
            goal=1
        else:
            goal=0
        return goal
    
    def penaleschance(self):
        chance=random.randint(self.passing,120)
        if chance>90:
            goal=1
        else:
            goal=0
        return goal






def penalesdefinitivos(player1,player2):
    goaloc=0
    goalvis=0
    keepgoing=True
    i=0
    while keepgoing:
        if i<=5:
            goaloc+=player1.penaleschance()
            goalvis+=player2.penaleschance()
            i+=1
            if goalvis>=3 or goaloc>=3:
                if (goaloc==4 or goalvis==4) and abs(goaloc-goalvis)>=3:
                    if goaloc>goalvis:
                        print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                        print(f"Cantidad de penales: {i*2}")
                        return player1
                    else:
                        print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                        print(f"Cantidad de penales: {i*2}")
                        return player2
                elif (goaloc>4 or goalvis>4) and abs(goaloc-goalvis)>=2:
                    if goaloc>goalvis:
                        print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                        print(f"Cantidad de penales: {i*2}")
                        return player1
                    else:
                        print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                        print(f"Cantidad de penales: {i*2}")
                        return player2

        elif i<=10:
            goaloc+=player1.penaleschance()
            goalvis+=player2.penaleschance()
            i+=1
            if abs(goaloc-goalvis)>=2:
                if goaloc>goalvis:
                    print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                    print(f"Cantidad de penales: {i*2}")
                    return player1
                else:
                    print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                    print(f"Cantidad de penales: {i*2}")
                    return player2
        elif i>10:
            goaloc+=player1.penaleschance()
            goalvis+=player2.penaleschance()
            i+=1
            if abs(goaloc-goalvis)>=1:
                if goaloc>goalvis:
                    print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                    print(f"Cantidad de penales: {i*2}")
                    return player1
                else:
                    print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name}")
                    print(f"Cantidad de penales: {i*2}")
                    return player2
        else:
            print(f"Penales:   {player1.name}:{goaloc}     {goalvis}:{player2.name} BREAK")
            print(f"Cantidad de penales: {i*2}")
            break






def attackdeffence(player1,player2):
    localat=player1.offensive()
    visat=player2.offensive()
    localdef=player1.deffensive()
    visdef=player2.deffensive()

    gollocal=0
    golvisitante=0
    
    if (localat-visdef) > 4:
        gollocal=(localat-visdef)//5
    if (visat-localdef)>4:
         golvisitante=(visat-localdef)//5


    return [gollocal,golvisitante]


def golespelotaparada(player1,player2):
    localchances=player1.playmakechance()
    vischances=player2.playmakechance()
    goleslocales=0
    golesvisitante=0
    
    while localchances>=1:
        goleslocales+=player1.fkgoalchance()

        localchances-=1

    while vischances>=1:
        golesvisitante+=player2.fkgoalchance()

        vischances-=1

    return [goleslocales,golesvisitante]

def resultadopartido(player1,player2):
    listadegolesattdff=attackdeffence(player1,player2)
    listadegolesfk=golespelotaparada(player1,player2)
    goleslocales=listadegolesattdff[0]+listadegolesfk[0]
    golesvisitante=listadegolesattdff[1]+listadegolesfk[1]
    player1.gf+=goleslocales
    player2.gf+=golesvisitante
    player1.gc+=golesvisitante
    player2.gc+=goleslocales

    print("---"*50)
    print(f"Resultado definitivo: {player1.name}:{goleslocales}  {golesvisitante}:{player2.name}")
    
    return [goleslocales,golesvisitante]





argentina=Football("Argentina",86,81,82,84,83)
australia=Football("Australia",75,70,71,72,72)
belgica=Football("Bélgica",86,79,80,83,82)
brazil=Football("Brazil",81,79,80,80,80)
camerun=Football("Camerún",75,72,75,73,74)
canada=Football("Canadá",74,70,74,74,73)
costarica=Football("Costa Rica",73,74,73,73,73)
croacia=Football("Croacia",79,78,83,81,80)
dinamarca=Football("Dinamarca",76,78,82,79,79)
ecuador=Football("Ecuador",75,75,75,75,75)
inglaterra=Football("Inglaterra",85,83,83,84,84)
francia=Football("Francia",85,82,83,84,83)
alemania=Football("Alemania",82,82,85,83,83)
ghana=Football("Ghana",81,75,76,78,77)
iran=Football("Irán",81,72,73,77,75)
japon=Football("Japón",75,76,77,76,76)
corea=Football("Corea del Sur",79,75,74,77,76)
mejico=Football("Méjico",79,76,77,78,77)
marruecos=Football("Marruecos",78,77,73,76,76)
paisesbajos=Football("Paises Bajos",83,82,81,82,82)
polonia=Football("Polonia",80,74,76,78,77)
portugal=Football("Portugal",85,84,82,83,84)
qatar=Football("Catar",71,68,70,70,70)
saudi=Football("Arabia Saudita",71,71,72,71,71)
senegal=Football("Senegal",79,77,76,77,77)
serbia=Football("Serbia",80,75,80,80,78)
españa=Football("España",82,85,84,83,84)
suiza=Football("Suiza",77,78,78,77,78)
tunez=Football("Túnez",72,71,75,73,73)
estadosunidos=Football("Estados Unidos",76,75,76,75,76)
uruguay=Football("Uruguay",81,79,82,81,81)
gales=Football("Gales",76,73,74,75,74)





#Grupos
#qatar-ecuador-senegal-paisesbajos      A
#inglaterra-iran-estadosunidos-gales    B
#argentina-arabiasaudi-mejico-polonia   C
#francia-australia-dinamarca-tunez      D
#españa-costarica-alemania-japon        E
#belgica-canada-maruecos-croacia        F
#brazil-serbia-suiza-camerun            G
#portugal-ghana-uruguay-corea           H

import random

class Football:
    def __init__(self,name,attack,deffend,passing,freekick,playmake):
        self.name=name
        self.attack=attack
        self.deffend=deffend
        self.passing=passing
        self.freekick=freekick
        self.playmake=playmake

    def __str__(self):
        return f"{self.name}: AT {self.attack}, DF {self.deffend}, PAS {self.passing}, TL {self.freekick}, SG {self.playmake}"

def offensive(namelocal,namevisitante,atlocal,dflocal,atvisitante,dfvisitante):
    dadoatloc=random.randint(atlocal,100)
    dadodefvis=random.randint(dfvisitante,100)
    dadodefloc=random.randint(dflocal,100)
    dadoatvis=random.randint(atvisitante,100)
    gollocal=0
    golvisitante=0
    
    if (dadoatloc-dadodefvis) > 4:
        gollocal=(dadoatloc-dadodefvis)//5
    if (dadoatvis-dadodefloc)>4:
         golvisitante=(dadoatvis-dadodefloc)//5

    print(f"{namelocal}: AT {dadoatloc} DF {dadodefloc}")
    print(f"{namevisitante}: AT {dadoatvis} DF {dadodefvis}")
    print(f"Local {dadoatloc-dadodefvis}")
    print(f"Visitante {dadoatvis-dadodefloc}")
    print(f"Resultado: {namelocal}: {gollocal} / {golvisitante} :{namevisitante}")







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
maruecos=Football("Marruecos",78,77,73,76,76)
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



offensive(argentina.name,inglaterra.name,argentina.attack,argentina.deffend,inglaterra.attack,inglaterra.deffend)

#Grupos
#qatar-ecuador-senegal-paisesbajos      A
#inglaterra-iran-estadosunidos-gales    B
#argentina-arabiasaudi-mejico-polonia   C
#francia-australia-dinamarca-tunez      D
#españa-costarica-alemania-japon        E
#belgica-canada-maruecos-croacia        F
#brazil-serbia-suiza-camerun            G
#portugal-ghana-uruguay-corea           H

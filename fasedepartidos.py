from simulacionmundialfifa import *


grupo_a=[ecuador,paisesbajos,senegal,qatar]
grupo_b=[estadosunidos,gales,inglaterra,iran]
grupo_c=[argentina,mejico,polonia,saudi]
grupo_d=[australia,dinamarca,francia,tunez]
grupo_e=[alemania,costarica,españa,japon]
grupo_f=[belgica,canada,croacia,marruecos]
grupo_g=[brazil,camerun,serbia,suiza]
grupo_h=[corea,ghana,portugal,uruguay]

def checkresultado(local,vis,game):
    if game[0]>game[1]:
        local.grouppoints+=3
    elif game[0]==game[1]:
        local.grouppoints+=1
        vis.grouppoints+=1
    elif game[0]<game[1]:
        vis.grouppoints+=3
    return local.grouppoints,local.grouppoints

#define los puntos del grupo
#falta resolver los empates en puntos
def definirpuntosgrupo(grupo):
    jugador1=grupo[0]
    jugador2=grupo[1]
    jugador3=grupo[2]
    jugador4=grupo[3]
    j1vsj2=resultadopartido(jugador1,jugador2)
    j1vsj3=resultadopartido(jugador1,jugador3)
    j1vsj4=resultadopartido(jugador1,jugador4)
    j2vsj3=resultadopartido(jugador2,jugador3)
    j2vsj4=resultadopartido(jugador2,jugador4)
    j3vsj4=resultadopartido(jugador3,jugador4)
    
    checkresultado(jugador1,jugador2,j1vsj2)
    checkresultado(jugador1,jugador3,j1vsj3)
    checkresultado(jugador1,jugador4,j1vsj4)
    checkresultado(jugador2,jugador3,j2vsj3)
    checkresultado(jugador2,jugador4,j2vsj4)
    checkresultado(jugador3,jugador4,j3vsj4)

    grupo.sort(key=lambda x: x.grouppoints,reverse=True)
    primerlugar=grupo[0]
    segundolugar=grupo[1]
    tercerlugar=grupo[2]
    cuartolugar=grupo[3]
    
    return [primerlugar,segundolugar,tercerlugar,cuartolugar]
    
def desempatargrupo(listadeganadores):
    ganadores=listadeganadores
    if listadeganadores[0].grouppoints==listadeganadores[2].grouppoints:
        if (listadeganadores[0].gf-listadeganadores[0].gc)>(listadeganadores[2].gf-listadeganadores[2].gc):
            if (listadeganadores[0].gf-listadeganadores[0].gc)>(listadeganadores[1].gf-listadeganadores[1].gc):
                if (listadeganadores[1].gf-listadeganadores[1].gc)>(listadeganadores[2].gf-listadeganadores[2].gc):
                    ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
                elif (listadeganadores[1].gf-listadeganadores[1].gc)<(listadeganadores[2].gf-listadeganadores[2].gc):
                    ganadores=[listadeganadores[0],listadeganadores[2],listadeganadores[1],listadeganadores[3]]
                else:
                    ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
            elif (listadeganadores[0].gf-listadeganadores[0].gc)<(listadeganadores[1].gf-listadeganadores[1].gc):
                ganadores=[listadeganadores[1],listadeganadores[0],listadeganadores[2],listadeganadores[3]]

        elif (listadeganadores[0].gf-listadeganadores[0].gc)>(listadeganadores[1].gf-listadeganadores[1].gc):
                if (listadeganadores[1].gf-listadeganadores[1].gc)>(listadeganadores[2].gf-listadeganadores[2].gc):
                    ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
                elif (listadeganadores[1].gf-listadeganadores[1].gc)<(listadeganadores[2].gf-listadeganadores[2].gc):
                    ganadores=[listadeganadores[0],listadeganadores[2],listadeganadores[1],listadeganadores[3]]
                else:
                    ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]

    elif listadeganadores[0].grouppoints==listadeganadores[1].grouppoints:
        if (listadeganadores[0].gf-listadeganadores[0].gc)>(listadeganadores[1].gf-listadeganadores[1].gc):
            ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
        elif (listadeganadores[0].gf-listadeganadores[0].gc)<(listadeganadores[1].gf-listadeganadores[1].gc):
            ganadores=[listadeganadores[1],listadeganadores[0],listadeganadores[2],listadeganadores[3]]
        else:
            ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
    elif listadeganadores[1].grouppoints==listadeganadores[2].grouppoints:
        if (listadeganadores[1].gf-listadeganadores[1].gc)>(listadeganadores[2].gf-listadeganadores[2].gc):
            ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
        elif (listadeganadores[1].gf-listadeganadores[1].gc)<(listadeganadores[2].gf-listadeganadores[2].gc):
            ganadores=[listadeganadores[0],listadeganadores[2],listadeganadores[1],listadeganadores[3]]
        else:
            ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
        
    else:
        ganadores=listadeganadores
    

    if listadeganadores[2].grouppoints==listadeganadores[3].grouppoints:
        if (listadeganadores[2].gf-listadeganadores[2].gc)>(listadeganadores[3].gf-listadeganadores[3].gc):
            ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[2],listadeganadores[3]]
        elif (listadeganadores[2].gf-listadeganadores[2].gc)<(listadeganadores[3].gf-listadeganadores[3].gc): 
            ganadores=[listadeganadores[0],listadeganadores[1],listadeganadores[3],listadeganadores[2]]

    
    print()
    print("-"*60)
    print(f"{ganadores[0].name}| puntos: {ganadores[0].grouppoints} | GF: {ganadores[0].gf} | GC: {ganadores[0].gc} | DG: {ganadores[0].gf - ganadores[0].gc}")
    print(f"{ganadores[1].name}| puntos: {ganadores[1].grouppoints} | GF: {ganadores[1].gf} | GC: {ganadores[1].gc} | DG: {ganadores[1].gf - ganadores[1].gc}")
    print(f"{ganadores[2].name}| puntos: {ganadores[2].grouppoints} | GF: {ganadores[2].gf} | GC: {ganadores[2].gc} | DG: {ganadores[2].gf - ganadores[2].gc}")
    print(f"{ganadores[3].name}| puntos: {ganadores[3].grouppoints} | GF: {ganadores[3].gf} | GC: {ganadores[3].gc} | DG: {ganadores[3].gf - ganadores[3].gc}")
    print("-"*60)

    return ganadores

def ganadordelpartido(player1,player2):
    goles=resultadopartido(player1,player2)
    if goles[0]>goles[1]:
        return player1

    elif goles[0]<goles[1]:
        return player2
        
    elif goles[0]==goles[1]:
        ganador=penales(player1,player2)
        return ganador
        
        
    




print()
grupo_a_partidos=definirpuntosgrupo(grupo_a)
grupo_a_definido=desempatargrupo(grupo_a_partidos)

grupo_b_partidos=definirpuntosgrupo(grupo_b)
grupo_b_definido=desempatargrupo(grupo_b_partidos)

grupo_c_partidos=definirpuntosgrupo(grupo_c)
grupo_c_definido=desempatargrupo(grupo_c_partidos)

grupo_d_partidos=definirpuntosgrupo(grupo_d)
grupo_d_definido=desempatargrupo(grupo_d_partidos)

grupo_e_partidos=definirpuntosgrupo(grupo_e)
grupo_e_definido=desempatargrupo(grupo_e_partidos)

grupo_f_partidos=definirpuntosgrupo(grupo_f)
grupo_f_definido=desempatargrupo(grupo_f_partidos)

grupo_g_partidos=definirpuntosgrupo(grupo_g)
grupo_g_definido=desempatargrupo(grupo_g_partidos)

grupo_h_partidos=definirpuntosgrupo(grupo_h)
grupo_h_definido=desempatargrupo(grupo_h_partidos)

#Como se enfrentan en las brakets según su posición en los grupos
#1avs2b --|(octavos)
#1cvs2d --|
#         |  
#         --- vs ---  | (cuartos)
#         --- vs ---  |
#         |           |
#         |           |
#1evs2f --|           | 
#1gvs2h --|           --- vs ---|(semifinal)
#                                --- vs ---  (final)
#                     --- vs ---|(semifinal)
#1bvs2a --|           |
#1dvs2c --|           |          --- vs --- (tercerlugar)
#         |           |
#         |           |
#         --- vs ---  | (cuartos)
#         --- vs ---  |
#         |
#         | 
#1fvs2e --|
#1hvs2g --|(octavos)

primeroctavo=[grupo_a_definido[0],grupo_b_definido[1]]
segundooctavo=[grupo_c_definido[0],grupo_d_definido[1]]

terceroctavo=[grupo_e_definido[0],grupo_f_definido[1]]
cuartooctavo=[grupo_g_definido[0],grupo_h_definido[1]]

quitooctavo=[grupo_b_definido[0],grupo_a_definido[1]]
sextooctavo=[grupo_d_definido[0],grupo_c_definido[1]]

septimooctavo=[grupo_f_definido[0],grupo_e_definido[1]]
octavooctavo=[grupo_h_definido[0],grupo_g_definido[1]]
print()
print("Octavos de final -----------------------------")
gprimer_octavo=ganadordelpartido(primeroctavo[0],primeroctavo[1])
gsegundo_octavo=ganadordelpartido(segundooctavo[0],segundooctavo[1])
gtercero_octavo=ganadordelpartido(terceroctavo[0],terceroctavo[1])
gcuarto_octavo=ganadordelpartido(cuartooctavo[0],cuartooctavo[1])
gquinto_octavo=ganadordelpartido(quitooctavo[0],quitooctavo[1])
gsexto_octavo=ganadordelpartido(sextooctavo[0],sextooctavo[1])
gseptimo_octavo=ganadordelpartido(septimooctavo[0],septimooctavo[1])
goctavo_octavo=ganadordelpartido(octavooctavo[0],octavooctavo[1])
print("Octavos de final -----------------------------")

primercuarto=[gprimer_octavo,gsegundo_octavo]
segundocuarto=[gtercero_octavo,gcuarto_octavo]
print()
tercercuarto=[gquinto_octavo,gsexto_octavo]
cuartocuarto=[gseptimo_octavo,goctavo_octavo]
print("Cuartos de final -----------------------------")
gprimer_cuarto=ganadordelpartido(primercuarto[0],primercuarto[1])
gsegundo_cuarto=ganadordelpartido(segundocuarto[0],segundocuarto[1])
gtercer_cuarto=ganadordelpartido(tercercuarto[0],tercercuarto[1])
gcuarto_cuarto=ganadordelpartido(cuartocuarto[0],cuartocuarto[1])
print("Cuartos de final -----------------------------")
primerasemifinal=[gprimer_cuarto,gsegundo_cuarto]
segundasemifinal=[gtercer_cuarto,gcuarto_cuarto]
print()
print("Semifinal ------------------------------------")
gprimera_semifinal=ganadordelpartido(primerasemifinal[0],primerasemifinal[1])
gsegunda_semifinal=ganadordelpartido(segundasemifinal[0],segundasemifinal[1])
print("Semifinal ------------------------------------")
final=[gprimera_semifinal,gsegunda_semifinal]
print()
print("Final ----------------------------------------")
g_final=ganadordelpartido(final[0],final[1])
print("Final ----------------------------------------")
print("^"*60)
print()
print(f"El ganador de esta edición del mundial es: {g_final}")
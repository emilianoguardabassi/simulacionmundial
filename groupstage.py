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


def definirgrupo(grupo):
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
    
    print()
    print(f"{grupo[0].name}| puntos: {grupo[0].grouppoints} | GF: {grupo[0].gf} | GC: {grupo[0].gc} | DG: {grupo[0].gf - grupo[0].gc}")
    print(f"{grupo[1].name}| puntos: {grupo[1].grouppoints} | GF: {grupo[1].gf} | GC: {grupo[1].gc} | DG: {grupo[1].gf - grupo[1].gc}")
    print(f"{grupo[2].name}| puntos: {grupo[2].grouppoints} | GF: {grupo[2].gf} | GC: {grupo[2].gc} | DG: {grupo[2].gf - grupo[2].gc}")
    print(f"{grupo[3].name}| puntos: {grupo[3].grouppoints} | GF: {grupo[3].gf} | GC: {grupo[3].gc} | DG: {grupo[3].gf - grupo[3].gc}")




print()
definirgrupo(grupo_h)

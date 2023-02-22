from datafifa import *
import xlsxwriter

workbook=xlsxwriter.Workbook("/home/emiliano/Documentos/proyectos/fifaproject/resumenmundial.xlsx")
worksheet1=workbook.add_worksheet("PrimerHoja")
worksheet2=workbook.add_worksheet("SegundaHoja")


grupo_a=[ecuador,paisesbajos,senegal,qatar]
grupo_b=[estadosunidos,gales,inglaterra,iran]
grupo_c=[argentina,mejico,polonia,saudi]
grupo_d=[australia,dinamarca,francia,tunez]
grupo_e=[alemania,costarica,españa,japon]
grupo_f=[belgica,canada,croacia,marruecos]
grupo_g=[brazil,camerun,serbia,suiza]
grupo_h=[corea,ghana,portugal,uruguay]


def xlsxpartidos(fila,columna,grupo): #Genera grupo en xlsx

    primer=grupo[1][0]
    segundo=grupo[1][1]
    tercero=grupo[1][2]
    cuarto=grupo[1][3]
    quinto=grupo[1][4]
    sexto=grupo[1][5]


    worksheet2.write(fila,columna,f"{primer[1][0]}: {primer[0][0]}VS{primer[0][1]} :{primer[1][1]}")
    worksheet2.write(fila+1,columna,f"{segundo[1][0]}: {segundo[0][0]}VS{segundo[0][1]} :{segundo[1][1]}")
    worksheet2.write(fila+2,columna,f"{tercero[1][0]}: {tercero[0][0]}VS{tercero[0][1]} :{tercero[1][1]}")
    worksheet2.write(fila+3,columna,f"{cuarto[1][0]}: {cuarto[0][0]}VS{cuarto[0][1]} :{cuarto[1][1]}")
    worksheet2.write(fila+4,columna,f"{quinto[1][0]}: {quinto[0][0]}VS{quinto[0][1]} :{quinto[1][1]}")
    worksheet2.write(fila+5,columna,f"{sexto[1][0]}: {sexto[0][0]}VS{sexto[0][1]} :{sexto[1][1]}")


def excelgrupos(fila,columna,grupo): #Genera grupo en xlsx

    worksheet1.write(fila,columna,f"{grupo[0].name}")
    worksheet1.write(fila,columna+1,f"{grupo[0].grouppoints}")
    worksheet1.write(fila,columna+2,f"{grupo[0].gf}")
    worksheet1.write(fila,columna+3,f"{grupo[0].gc}")
    worksheet1.write(fila,columna+4,f"{grupo[0].gf-grupo[0].gc}")

    worksheet1.write(fila+1,columna,f"{grupo[1].name}")
    worksheet1.write(fila+1,columna+1,f"{grupo[1].grouppoints}")
    worksheet1.write(fila+1,columna+2,f"{grupo[1].gf}")
    worksheet1.write(fila+1,columna+3,f"{grupo[1].gc}")
    worksheet1.write(fila+1,columna+4,f"{grupo[1].gf-grupo[1].gc}")

    worksheet1.write(fila+2,columna,f"{grupo[2].name}")
    worksheet1.write(fila+2,columna+1,f"{grupo[2].grouppoints}")
    worksheet1.write(fila+2,columna+2,f"{grupo[2].gf}")
    worksheet1.write(fila+2,columna+3,f"{grupo[2].gc}")
    worksheet1.write(fila+2,columna+4,f"{grupo[2].gf-grupo[2].gc}")

    worksheet1.write(fila+3,columna,f"{grupo[3].name}")
    worksheet1.write(fila+3,columna+1,f"{grupo[3].grouppoints}")
    worksheet1.write(fila+3,columna+2,f"{grupo[3].gf}")
    worksheet1.write(fila+3,columna+3,f"{grupo[3].gc}")
    worksheet1.write(fila+3,columna+4,f"{grupo[3].gf-grupo[3].gc}")



def checkresultado(local,vis,game): #Asigna puntos según el resultado del partido de grupos
    if game[0]>game[1]:
        local.grouppoints+=3
    elif game[0]==game[1]:
        local.grouppoints+=1
        vis.grouppoints+=1
    elif game[0]<game[1]:
        vis.grouppoints+=3
    return local.grouppoints,local.grouppoints


def definirpuntosgrupo(grupo): #Define los puntos de grupo
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
    
    checkresultado(jugador1,jugador2,j1vsj2[0])
    checkresultado(jugador1,jugador3,j1vsj3[0])
    checkresultado(jugador1,jugador4,j1vsj4[0])
    checkresultado(jugador2,jugador3,j2vsj3[0])
    checkresultado(jugador2,jugador4,j2vsj4[0])
    checkresultado(jugador3,jugador4,j3vsj4[0])

    grupo.sort(key=lambda x: x.grouppoints,reverse=True)
    primerlugar=grupo[0]
    segundolugar=grupo[1]
    tercerlugar=grupo[2]
    cuartolugar=grupo[3]
    
    return [[primerlugar,segundolugar,tercerlugar,cuartolugar],[j1vsj2,j1vsj3,j1vsj4,j2vsj3,j2vsj4,j3vsj4]]

def desempatarcuadruple(p,s,t,c):
    desempate=desempatargrupoDG([p,s,t,c])
    return desempate


def desempatartriple(p,s,t):
    desempate=desempatargrupoDG([p,s,t,sample])
    return desempate

def desempatardoble(p,s):
    desempate=desempatargrupoDG([p,s,sample,sample])
    return desempate

def desempatartripleinferior(s,t,c):
    desempate=desempatargrupoDG([samplepositiv,s,t,c])
    return desempate

def desempatardobleinferior(t,c):
    desempate=desempatargrupoDG([samplepositiv,samplepositiv,t,c])
    return desempate

def desempatarmedio(s,t):
    desempate=desempatargrupoDG([samplepositiv,s,t,sample])
    return desempate
    
def desempatargrupoDG(listadeganadores):

    p_lugar=listadeganadores[0]
    s_lugar=listadeganadores[1]
    t_lugar=listadeganadores[2]
    c_lugar=listadeganadores[3]

    dg_p_lugar=[p_lugar.gf-p_lugar.gc,p_lugar]
    dg_s_lugar=[s_lugar.gf-s_lugar.gc,s_lugar]
    dg_t_lugar=[t_lugar.gf-t_lugar.gc,t_lugar]
    dg_c_lugar=[c_lugar.gf-c_lugar.gc,c_lugar]

    dg_list=[dg_p_lugar,dg_s_lugar,dg_t_lugar,dg_c_lugar]
    dg_list_sorted=sorted(dg_list,key=lambda x:x[0],reverse=True)

    n_p_lugar=dg_list_sorted[0]
    n_s_lugar=dg_list_sorted[1]
    n_t_lugar=dg_list_sorted[2]
    n_c_lugar=dg_list_sorted[3]


    ganadores=[n_p_lugar[1],n_s_lugar[1],n_t_lugar[1],n_c_lugar[1]]
    return ganadores
    

def desempatargrupo(g):

    if g[0].grouppoints==g[1].grouppoints==g[2].grouppoints==g[3].grouppoints:
        ganadores=desempatarcuadruple(g[0],g[1],g[2],g[3])
    elif g[0].grouppoints==g[1].grouppoints==g[2].grouppoints:
        ganadores=desempatartriple(g[0],g[1],g[2])
        ganadores=[ganadores[0],ganadores[1],ganadores[2],g[3]]
    elif g[0].grouppoints==g[1].grouppoints:
        ganadores=desempatardoble(g[0],g[1])
        ganadores=[ganadores[0],ganadores[1],g[2],g[3]]
        if  g[2].grouppoints==g[3].grouppoints:
            ganadores=desempatardobleinferior(g[2],g[3])
            ganadores=[g[0],g[1],ganadores[2],ganadores[3]]
    elif g[1].grouppoints==g[2].grouppoints==g[3].grouppoints:
        ganadores=desempatartripleinferior(g[1],g[2],g[3])
        ganadores=[g[0],ganadores[1],ganadores[2],ganadores[3]]
    elif g[2].grouppoints==g[3].grouppoints:
        ganadores=desempatardobleinferior(g[2],g[3])
        ganadores=[g[0],g[1],ganadores[2],ganadores[3]]
    elif g[1].grouppoints==g[2].grouppoints:
        ganadores=desempatarmedio(g[1],g[2])
        ganadores=[g[0],ganadores[1],ganadores[2],g[3]]
    else:
        ganadores=g



    print()
    print("-"*60)
    print(f"{ganadores[0].name}| puntos: {ganadores[0].grouppoints} | GF: {ganadores[0].gf} | GC: {ganadores[0].gc} | DG: {ganadores[0].gf - ganadores[0].gc}")
    print(f"{ganadores[1].name}| puntos: {ganadores[1].grouppoints} | GF: {ganadores[1].gf} | GC: {ganadores[1].gc} | DG: {ganadores[1].gf - ganadores[1].gc}")
    print(f"{ganadores[2].name}| puntos: {ganadores[2].grouppoints} | GF: {ganadores[2].gf} | GC: {ganadores[2].gc} | DG: {ganadores[2].gf - ganadores[2].gc}")
    print(f"{ganadores[3].name}| puntos: {ganadores[3].grouppoints} | GF: {ganadores[3].gf} | GC: {ganadores[3].gc} | DG: {ganadores[3].gf - ganadores[3].gc}")
    print("-"*60)

    return ganadores

def ganadordelpartido(player1,player2): #Resultados de partidos eliminatorios
    goles=resultadopartido(player1,player2)
    if goles[0][0]>goles[0][1]:
        return [player1,goles[0],goles[1],"",""]

    elif goles[0][0]<goles[0][1]:
        return [player2,goles[0],goles[1],"",""]
        
    elif goles[0][0]==goles[0][1]:
        ganador=penalesdefinitivos(player1,player2)
        return [ganador[0],goles[0],goles[1],ganador[1],ganador[2]]
        
        
#definición de grupos
print()
grupo_a_partidos=definirpuntosgrupo(grupo_a)
grupo_a_definido=desempatargrupo(grupo_a_partidos[0])

grupo_b_partidos=definirpuntosgrupo(grupo_b)
grupo_b_definido=desempatargrupo(grupo_b_partidos[0])

grupo_c_partidos=definirpuntosgrupo(grupo_c)
grupo_c_definido=desempatargrupo(grupo_c_partidos[0])

grupo_d_partidos=definirpuntosgrupo(grupo_d)
grupo_d_definido=desempatargrupo(grupo_d_partidos[0])

grupo_e_partidos=definirpuntosgrupo(grupo_e)
grupo_e_definido=desempatargrupo(grupo_e_partidos[0])

grupo_f_partidos=definirpuntosgrupo(grupo_f)
grupo_f_definido=desempatargrupo(grupo_f_partidos[0])

grupo_g_partidos=definirpuntosgrupo(grupo_g)
grupo_g_definido=desempatargrupo(grupo_g_partidos[0])

grupo_h_partidos=definirpuntosgrupo(grupo_h)
grupo_h_definido=desempatargrupo(grupo_h_partidos[0])


#resultado partidos de grupos xlsx
worksheet2.write(0,0,"GrupoA")
xlsxpartidos(1,0,grupo_a_partidos)
worksheet2.write(9,0,"GrupoB")
xlsxpartidos(10,0,grupo_b_partidos)
worksheet2.write(18,0,"GrupoC")
xlsxpartidos(19,0,grupo_c_partidos)
worksheet2.write(27,0,"GrupoD")
xlsxpartidos(28,0,grupo_d_partidos)
worksheet2.write(36,0,"GrupoE")
xlsxpartidos(37,0,grupo_e_partidos)
worksheet2.write(45,0,"GrupoF")
xlsxpartidos(46,0,grupo_f_partidos)
worksheet2.write(54,0,"GrupoG")
xlsxpartidos(55,0,grupo_g_partidos)
worksheet2.write(63,0,"GrupoH")
xlsxpartidos(64,0,grupo_h_partidos)


#Armado xlsx grupos
worksheet1.write(0,0,"GrupoA")
worksheet1.write(1,0,"País")
worksheet1.write(1,1,"Puntos")
worksheet1.write(1,2,"GF")
worksheet1.write(1,3,"GC")
worksheet1.write(1,4,"DG")
excelgrupos(2,0,grupo_a_definido)

worksheet1.write(7,0,"GrupoB")
worksheet1.write(8,0,"País")
worksheet1.write(8,1,"Puntos")
worksheet1.write(8,2,"GF")
worksheet1.write(8,3,"GC")
worksheet1.write(8,4,"DG")
excelgrupos(9,0,grupo_b_definido)

worksheet1.write(14,0,"GrupoC")
worksheet1.write(15,0,"País")
worksheet1.write(15,1,"Puntos")
worksheet1.write(15,2,"GF")
worksheet1.write(15,3,"GC")
worksheet1.write(15,4,"DG")
excelgrupos(16,0,grupo_c_definido)

worksheet1.write(21,0,"GrupoD")
worksheet1.write(22,0,"País")
worksheet1.write(22,1,"Puntos")
worksheet1.write(22,2,"GF")
worksheet1.write(22,3,"GC")
worksheet1.write(22,4,"DG")
excelgrupos(23,0,grupo_d_definido)

worksheet1.write(28,0,"GrupoE")
worksheet1.write(29,0,"País")
worksheet1.write(29,1,"Puntos")
worksheet1.write(29,2,"GF")
worksheet1.write(29,3,"GC")
worksheet1.write(29,4,"DG")
excelgrupos(30,0,grupo_e_definido)

worksheet1.write(35,0,"GrupoF")
worksheet1.write(36,0,"País")
worksheet1.write(36,1,"Puntos")
worksheet1.write(36,2,"GF")
worksheet1.write(36,3,"GC")
worksheet1.write(36,4,"DG")
excelgrupos(37,0,grupo_f_definido)

worksheet1.write(42,0,"GrupoG")
worksheet1.write(43,0,"País")
worksheet1.write(43,1,"Puntos")
worksheet1.write(43,2,"GF")
worksheet1.write(43,3,"GC")
worksheet1.write(43,4,"DG")
excelgrupos(44,0,grupo_g_definido)

worksheet1.write(49,0,"GrupoH")
worksheet1.write(50,0,"País")
worksheet1.write(50,1,"Puntos")
worksheet1.write(50,2,"GF")
worksheet1.write(50,3,"GC")
worksheet1.write(50,4,"DG")
excelgrupos(51,0,grupo_h_definido)


primeroctavo=[grupo_a_definido[0],grupo_b_definido[1]]
segundooctavo=[grupo_c_definido[0],grupo_d_definido[1]]

terceroctavo=[grupo_e_definido[0],grupo_f_definido[1]]
cuartooctavo=[grupo_g_definido[0],grupo_h_definido[1]]

quitooctavo=[grupo_b_definido[0],grupo_a_definido[1]]
sextooctavo=[grupo_d_definido[0],grupo_c_definido[1]]

septimooctavo=[grupo_f_definido[0],grupo_e_definido[1]]
octavooctavo=[grupo_h_definido[0],grupo_g_definido[1]]
print()
print("*"*60)
print()
print("Octavos de final -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print()
gprimer_octavo=ganadordelpartido(primeroctavo[0],primeroctavo[1])
gsegundo_octavo=ganadordelpartido(segundooctavo[0],segundooctavo[1])
gtercero_octavo=ganadordelpartido(terceroctavo[0],terceroctavo[1])
gcuarto_octavo=ganadordelpartido(cuartooctavo[0],cuartooctavo[1])
gquinto_octavo=ganadordelpartido(quitooctavo[0],quitooctavo[1])
gsexto_octavo=ganadordelpartido(sextooctavo[0],sextooctavo[1])
gseptimo_octavo=ganadordelpartido(septimooctavo[0],septimooctavo[1])
goctavo_octavo=ganadordelpartido(octavooctavo[0],octavooctavo[1])
print()
print("Octavos de final -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")

primercuarto=[gprimer_octavo[0],gsegundo_octavo[0]]
segundocuarto=[gtercero_octavo[0],gcuarto_octavo[0]]
print()
tercercuarto=[gquinto_octavo[0],gsexto_octavo[0]]
cuartocuarto=[gseptimo_octavo[0],goctavo_octavo[0]]
print()
print("*"*60)
print()
print("Cuartos de final -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print()
gprimer_cuarto=ganadordelpartido(primercuarto[0],primercuarto[1])
gsegundo_cuarto=ganadordelpartido(segundocuarto[0],segundocuarto[1])
gtercer_cuarto=ganadordelpartido(tercercuarto[0],tercercuarto[1])
gcuarto_cuarto=ganadordelpartido(cuartocuarto[0],cuartocuarto[1])
print()
print("Cuartos de final -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
primerasemifinal=[gprimer_cuarto[0],gsegundo_cuarto[0]]
segundasemifinal=[gtercer_cuarto[0],gcuarto_cuarto[0]]
print()
print("*"*60)
print()
print("Semifinal -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
gprimera_semifinal=ganadordelpartido(primerasemifinal[0],primerasemifinal[1])
gsegunda_semifinal=ganadordelpartido(segundasemifinal[0],segundasemifinal[1])
print("Semifinal -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
final=[gprimera_semifinal[0],gsegunda_semifinal[0]]
print()
print("*"*60)
print()
print("Final -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print()
g_final=ganadordelpartido(final[0],final[1])
print()
print("Final -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
print("^"*60)
print()
print(f"El ganador de esta edición del mundial es: {g_final[0]}")
print(f"{g_final[0].name} logró asegurar {g_final[0].gf} goles y recibió {g_final[0].gc} goles")

#Armado xslx brakets
worksheet1.write(8,7,f"{primeroctavo[0].name}:{gprimer_octavo[1][0]} VS {gprimer_octavo[1][1]}:{primeroctavo[1].name} ({gprimer_octavo[3]} : {gprimer_octavo[4]})")
worksheet1.write(10,7,f"{segundooctavo[0].name}:{gsegundo_octavo[1][0]} VS {gsegundo_octavo[1][1]}:{segundooctavo[1].name} ({gsegundo_octavo[3]} : {gsegundo_octavo[4]})")
worksheet1.write(14,7,f"{terceroctavo[0].name}:{gtercero_octavo[1][0]} VS {gtercero_octavo[1][1]}:{terceroctavo[1].name} ({gtercero_octavo[3]} : {gtercero_octavo[4]})")
worksheet1.write(16,7,f"{cuartooctavo[0].name}:{gcuarto_octavo[1][0]} VS {gcuarto_octavo[1][1]}:{cuartooctavo[1].name} ({gcuarto_octavo[3]} : {gcuarto_octavo[4]})")
worksheet1.write(21,7,f"{quitooctavo[0].name}:{gquinto_octavo[1][0]} VS {gquinto_octavo[1][1]}:{quitooctavo[1].name} ({gquinto_octavo[3]} : {gquinto_octavo[4]})")
worksheet1.write(23,7,f"{sextooctavo[0].name}:{gsexto_octavo[1][0]} VS {gsexto_octavo[1][1]}:{sextooctavo[1].name} ({gsexto_octavo[3]} : {gsexto_octavo[4]})")
worksheet1.write(27,7,f"{septimooctavo[0].name}:{gseptimo_octavo[1][0]} VS {gseptimo_octavo[1][1]}:{septimooctavo[1].name} ({gseptimo_octavo[3]} : {gseptimo_octavo[4]})")
worksheet1.write(29,7,f"{octavooctavo[0].name}:{goctavo_octavo[1][0]} VS {goctavo_octavo[1][1]}:{octavooctavo[1].name} ({goctavo_octavo[3]} : {goctavo_octavo[4]})")

worksheet1.write(9,9,f"{primercuarto[0].name}:{gprimer_cuarto[1][0]} VS {gprimer_cuarto[1][1]}:{primercuarto[1].name} ({gprimer_cuarto[3]} : {gprimer_cuarto[4]})")
worksheet1.write(15,9,f"{segundocuarto[0].name}:{gsegundo_cuarto[1][0]} VS {gsegundo_cuarto[1][1]}:{segundocuarto[1].name} ({gsegundo_cuarto[3]} : {gsegundo_cuarto[4]})")
worksheet1.write(22,9,f"{tercercuarto[0].name}:{gtercer_cuarto[1][0]} VS {gtercer_cuarto[1][1]}:{tercercuarto[1].name} ({gtercer_cuarto[3]} : {gtercer_cuarto[4]})")
worksheet1.write(28,9,f"{cuartocuarto[0].name}:{gcuarto_cuarto[1][0]} VS {gcuarto_cuarto[1][1]}:{cuartocuarto[1].name} ({gcuarto_cuarto[3]} : {gcuarto_cuarto[4]})")

worksheet1.write(12,11,f"{primerasemifinal[0].name}:{gprimera_semifinal[1][0]} VS {gprimera_semifinal[1][1]}:{primerasemifinal[1].name} ({gprimera_semifinal[3]} : {gprimera_semifinal[4]})")
worksheet1.write(25,11,f"{segundasemifinal[0].name}:{gsegunda_semifinal[1][0]} VS {gsegunda_semifinal[1][1]}:{segundasemifinal[1].name} ({gsegunda_semifinal[3]} : {gsegunda_semifinal[4]})")

worksheet1.write(19,13,f"{final[0].name}:{g_final[1][0]} VS {g_final[1][1]}:{final[1].name} ({g_final[3]} : {g_final[4]})")

worksheet1.write(19,14,f"Ganador:{g_final[0].name}!!")

worksheet1.set_column(7,7,34)
worksheet1.set_column(9,9,34)
worksheet1.set_column(11,11,34)
worksheet1.set_column(13,14,34)
worksheet1.set_column(0,0,16)
worksheet2.set_column(0,0,28)
workbook.close()





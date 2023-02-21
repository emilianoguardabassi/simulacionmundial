from datafifa import *
import xlsxwriter

workbook=xlsxwriter.Workbook("/home/emiliano/Documentos/proyectos/fifaproject/resumenmundial.xlsx")
worksheet=workbook.add_worksheet("PrimerHoja")


grupo_a=[ecuador,paisesbajos,senegal,qatar]
grupo_b=[estadosunidos,gales,inglaterra,iran]
grupo_c=[argentina,mejico,polonia,saudi]
grupo_d=[australia,dinamarca,francia,tunez]
grupo_e=[alemania,costarica,españa,japon]
grupo_f=[belgica,canada,croacia,marruecos]
grupo_g=[brazil,camerun,serbia,suiza]
grupo_h=[corea,ghana,portugal,uruguay]

def excelgrupos(fila,columna,grupo): #Genera grupo en xlsx

    worksheet.write(fila,columna,f"{grupo[0].name}")
    worksheet.write(fila,columna+1,f"{grupo[0].grouppoints}")
    worksheet.write(fila,columna+2,f"{grupo[0].gf}")
    worksheet.write(fila,columna+3,f"{grupo[0].gc}")
    worksheet.write(fila,columna+4,f"{grupo[0].gf-grupo[0].gc}")

    worksheet.write(fila+1,columna,f"{grupo[1].name}")
    worksheet.write(fila+1,columna+1,f"{grupo[1].grouppoints}")
    worksheet.write(fila+1,columna+2,f"{grupo[1].gf}")
    worksheet.write(fila+1,columna+3,f"{grupo[1].gc}")
    worksheet.write(fila+1,columna+4,f"{grupo[1].gf-grupo[1].gc}")

    worksheet.write(fila+2,columna,f"{grupo[2].name}")
    worksheet.write(fila+2,columna+1,f"{grupo[2].grouppoints}")
    worksheet.write(fila+2,columna+2,f"{grupo[2].gf}")
    worksheet.write(fila+2,columna+3,f"{grupo[2].gc}")
    worksheet.write(fila+2,columna+4,f"{grupo[2].gf-grupo[2].gc}")

    worksheet.write(fila+3,columna,f"{grupo[3].name}")
    worksheet.write(fila+3,columna+1,f"{grupo[3].grouppoints}")
    worksheet.write(fila+3,columna+2,f"{grupo[3].gf}")
    worksheet.write(fila+3,columna+3,f"{grupo[3].gc}")
    worksheet.write(fila+3,columna+4,f"{grupo[3].gf-grupo[3].gc}")



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

def ganadordelpartido(player1,player2): #Resultados de partidos eliminatorios
    goles=resultadopartido(player1,player2)
    if goles[0]>goles[1]:
        return [player1,goles[0],goles[1],"",""]

    elif goles[0]<goles[1]:
        return [player2,goles[0],goles[1],"",""]
        
    elif goles[0]==goles[1]:
        ganador=penalesdefinitivos(player1,player2)
        return [ganador[0],goles[0],goles[1],ganador[1],ganador[2]]
        
        
#definición de grupos
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


#Armado xslx grupos
worksheet.write(0,0,"GrupoA")
worksheet.write(1,0,"País")
worksheet.write(1,1,"Puntos")
worksheet.write(1,2,"GF")
worksheet.write(1,3,"GC")
worksheet.write(1,4,"DG")
excelgrupos(2,0,grupo_a_definido)

worksheet.write(7,0,"GrupoB")
worksheet.write(8,0,"País")
worksheet.write(8,1,"Puntos")
worksheet.write(8,2,"GF")
worksheet.write(8,3,"GC")
worksheet.write(8,4,"DG")
excelgrupos(9,0,grupo_b_definido)

worksheet.write(14,0,"GrupoC")
worksheet.write(15,0,"País")
worksheet.write(15,1,"Puntos")
worksheet.write(15,2,"GF")
worksheet.write(15,3,"GC")
worksheet.write(15,4,"DG")
excelgrupos(16,0,grupo_c_definido)

worksheet.write(21,0,"GrupoD")
worksheet.write(22,0,"País")
worksheet.write(22,1,"Puntos")
worksheet.write(22,2,"GF")
worksheet.write(22,3,"GC")
worksheet.write(22,4,"DG")
excelgrupos(23,0,grupo_d_definido)

worksheet.write(28,0,"GrupoE")
worksheet.write(29,0,"País")
worksheet.write(29,1,"Puntos")
worksheet.write(29,2,"GF")
worksheet.write(29,3,"GC")
worksheet.write(29,4,"DG")
excelgrupos(30,0,grupo_e_definido)

worksheet.write(35,0,"GrupoF")
worksheet.write(36,0,"País")
worksheet.write(36,1,"Puntos")
worksheet.write(36,2,"GF")
worksheet.write(36,3,"GC")
worksheet.write(36,4,"DG")
excelgrupos(37,0,grupo_f_definido)

worksheet.write(42,0,"GrupoG")
worksheet.write(43,0,"País")
worksheet.write(43,1,"Puntos")
worksheet.write(43,2,"GF")
worksheet.write(43,3,"GC")
worksheet.write(43,4,"DG")
excelgrupos(44,0,grupo_g_definido)

worksheet.write(49,0,"GrupoH")
worksheet.write(50,0,"País")
worksheet.write(50,1,"Puntos")
worksheet.write(50,2,"GF")
worksheet.write(50,3,"GC")
worksheet.write(50,4,"DG")
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
worksheet.write(8,7,f"{primeroctavo[0].name}:{gprimer_octavo[1]} VS {gprimer_octavo[2]}:{primeroctavo[1].name} ({gprimer_octavo[3]} : {gprimer_octavo[4]})")
worksheet.write(10,7,f"{segundooctavo[0].name}:{gsegundo_octavo[1]} VS {gsegundo_octavo[2]}:{segundooctavo[1].name} ({gsegundo_octavo[3]} : {gsegundo_octavo[4]})")
worksheet.write(14,7,f"{terceroctavo[0].name}:{gtercero_octavo[1]} VS {gtercero_octavo[2]}:{terceroctavo[1].name} ({gtercero_octavo[3]} : {gtercero_octavo[4]})")
worksheet.write(16,7,f"{cuartooctavo[0].name}:{gcuarto_octavo[1]} VS {gcuarto_octavo[2]}:{cuartooctavo[1].name} ({gcuarto_octavo[3]} : {gcuarto_octavo[4]})")
worksheet.write(21,7,f"{quitooctavo[0].name}:{gquinto_octavo[1]} VS {gquinto_octavo[2]}:{quitooctavo[1].name} ({gquinto_octavo[3]} : {gquinto_octavo[4]})")
worksheet.write(23,7,f"{sextooctavo[0].name}:{gsexto_octavo[1]} VS {gsexto_octavo[2]}:{sextooctavo[1].name} ({gsexto_octavo[3]} : {gsexto_octavo[4]})")
worksheet.write(27,7,f"{septimooctavo[0].name}:{gseptimo_octavo[1]} VS {gseptimo_octavo[2]}:{septimooctavo[1].name} ({gseptimo_octavo[3]} : {gseptimo_octavo[4]})")
worksheet.write(29,7,f"{octavooctavo[0].name}:{goctavo_octavo[1]} VS {goctavo_octavo[2]}:{octavooctavo[1].name} ({goctavo_octavo[3]} : {goctavo_octavo[4]})")

worksheet.write(9,9,f"{primercuarto[0].name}:{gprimer_cuarto[1]} VS {gprimer_cuarto[2]}:{primercuarto[1].name} ({gprimer_cuarto[3]} : {gprimer_cuarto[4]})")
worksheet.write(15,9,f"{segundocuarto[0].name}:{gsegundo_cuarto[1]} VS {gsegundo_cuarto[2]}:{segundocuarto[1].name} ({gsegundo_cuarto[3]} : {gsegundo_cuarto[4]})")
worksheet.write(22,9,f"{tercercuarto[0].name}:{gtercer_cuarto[1]} VS {gtercer_cuarto[2]}:{tercercuarto[1].name} ({gtercer_cuarto[3]} : {gtercer_cuarto[4]})")
worksheet.write(28,9,f"{cuartocuarto[0].name}:{gcuarto_cuarto[1]} VS {gcuarto_cuarto[2]}:{cuartocuarto[1].name} ({gcuarto_cuarto[3]} : {gcuarto_cuarto[4]})")

worksheet.write(12,11,f"{primerasemifinal[0].name}:{gprimera_semifinal[1]} VS {gprimera_semifinal[2]}:{primerasemifinal[1].name} ({gprimera_semifinal[3]} : {gprimera_semifinal[4]})")
worksheet.write(25,11,f"{segundasemifinal[0].name}:{gsegunda_semifinal[1]} VS {gsegunda_semifinal[2]}:{segundasemifinal[1].name} ({gsegunda_semifinal[3]} : {gsegunda_semifinal[4]})")

worksheet.write(19,13,f"{final[0].name}:{g_final[1]} VS {g_final[2]}:{final[1].name} ({g_final[3]} : {g_final[4]})")

worksheet.write(19,14,f"Ganador:{g_final[0].name}!!")

worksheet.set_column(7,7,34)
worksheet.set_column(9,9,34)
worksheet.set_column(11,11,34)
worksheet.set_column(13,14,34)
worksheet.set_column(0,0,16)
workbook.close()





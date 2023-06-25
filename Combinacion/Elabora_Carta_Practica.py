#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones_2 import cargaArchivo, fechaActual, elaboraCartaPractica
from datetime import datetime

#------------------------------------------------------------

hoy = datetime.now()
cadenaFecha = fechaActual(hoy)
archivoInicial = input("Ingresa el nombre del archivo .csv: ")
print()

DF1 = cargaArchivo(archivoInicial)

contadorCartas = 0
contadorNP = 0

for i in DF1.index:
    Entregada = str(DF1['Entregada'][i])
    Estudiante = str(DF1['Estudiante'][i])
    Preparacion = str(DF1['Preparacion'][i])
    Trabajo_E = str(DF1['Trabajo_E'][i])
    Participacion = str(DF1['Participacion'][i])
    Reporte = str(DF1['Reporte'][i])
    Conclusiones = str(DF1['Conclusiones'][i])
    Calificacion = str(DF1['Calificacion'][i])
    Comentarios = str(DF1['Comentarios'][i])

    if int(Entregada) == 1:
        if Estudiante == 'VASQUEZ CARRASCO CARLOS BARUCH':
            contadorCartas += 1
            print(Estudiante)

            elaboraCartaPractica(Estudiante, Preparacion, Trabajo_E, Participacion, Reporte, Conclusiones, Calificacion, Comentarios)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))

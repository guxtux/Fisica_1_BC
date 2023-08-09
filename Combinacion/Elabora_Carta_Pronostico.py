# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:41:40 2023

@author: gusto
"""

from Modulo_Funciones_2 import cargaArchivo, fechaActual, elaboraCartaConcentradoSemanal
from datetime import datetime

#------------------------------------------------------------

hoy = datetime.now()
cadenaFecha = fechaActual(hoy)
archivoInicial = "Pronostico_Fisica_1_NRC_240.csv"
print()

DF1 = cargaArchivo(archivoInicial)

contadorCartas = 0
contadorNP = 0

Semana =  '7'

for i in DF1.index:
    Estudiante = str(DF1['Estudiante'][i])
    Primer = str(DF1['Primer'][i])
    Segundo = str(DF1['Segundo'][i])
    Tercer = str(DF1['Tercer'][i])
    Pronostico = str(DF1['Pronostico'][i])
    
    #if Estudiante == 'REYES ROBLES NURIA':
    contadorCartas += 1
    print(Estudiante)
    elaboraCartaPronostico(Estudiante, Primer, Segundo, Tercer, Pronostico)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones_2 import cargaArchivo, fechaActual, elaboraCartaConcentrado
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
    Estudiante = str(DF1['Estudiante'][i])
    L_Tiempo = str(DF1['L_Tiempo'][i])
    Ejer_4 = str(DF1['Ejer_4'][i])
    SIU = str(DF1['SIU'][i])
    Not_Cient = str(DF1['Not_Cient'][i])
    M_Amb = str(DF1['M_Amb'][i])
    Puntos = str(DF1['Puntos'][i])
    Eval_Continua = str(DF1['Eval_Continua'][i])
    Practica_1 = str(DF1['Practica_1'][i])
    Practica_2 = str(DF1['Practica_2'][i])
    Laboratorio = str(DF1['Laboratorio'][i])
    
    contadorCartas += 1
    print(Estudiante)
    elaboraCartaConcentrado(Estudiante, L_Tiempo, Ejer_4, SIU, Not_Cient, M_Amb, Puntos, Eval_Continua, Practica_1, Practica_2, Laboratorio)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones import cargaArchivo, fechaActual, elaboracartaEvalContinua
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
    Nombre = str(DF1['Estudiante'][i])
    ETP = str(DF1['Ecs_Tiro_Parabolico'][i])
    Componente_Vector = str(DF1['Componente_Vector'][i])
    Componente_4_Vectores = str(DF1['Componente_4_Vectores'][i])
    Ejercicio_Trabajo = str(DF1['Ejercicio_Trabajo'][i])
    Kepler = str(DF1['Kepler'][i])
    O4A = str(DF1['Ordenar_4_aceleraciones'][i])
    Gravitacion = str(DF1['Gravitacion'][i])
    Puntos = str(DF1['Puntos'][i])
    Calificacion = str(DF1['Calificacion'][i])

    
    contadorCartas += 1
    print(Nombre)
    elaboracartaEvalContinua(Nombre, ETP, Componente_Vector, Componente_4_Vectores, Ejercicio_Trabajo, Kepler, O4A, Gravitacion, Puntos, Calificacion)
    
print()
print('Se elaboraron {0:} cartas con calificación y comentarios.'.format(contadorCartas))
# print('Se omitieron {0:} cartas con NP.'.format(contadorNP))

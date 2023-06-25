#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:01:11 2022

@author: gustavo
"""

from Modulo_Funciones import cargaArchivo, fechaActual, elaboraConstancia
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
    numeroCuenta = str(DF1['Cuenta'][i])
    alumno = str(DF1['Alumno'][i])
    pTareas = str(DF1['P_Tareas'][i])
    pExamen = str(DF1['P_Examen'][i])
    promedio = str(DF1['Promedio'][i])
    campana = str(DF1['Campana'][i])
    calificacionFinal = str(DF1['Final'][i])
    comentarios = str(DF1['Comentarios'][i])
    selloDigital = str(DF1['Clave_Hash256'][i])
    
    if calificacionFinal == 'NP':
        contadorNP += 1
        continue
    
    print(numeroCuenta, alumno)
    contadorCartas += 1
    elaboraConstancia(alumno, numeroCuenta, pTareas, pExamen, promedio, campana, calificacionFinal, comentarios, selloDigital, cadenaFecha)
    
print()
print('Se elaboraron {0:} cartas con calificación.'.format(contadorCartas))
print('Se omitieron {0:} cartas con NP.'.format(contadorNP))

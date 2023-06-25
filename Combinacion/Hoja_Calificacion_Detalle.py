# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
import csv
from numpy import array
import os

def calificacionCadena(final):
    calificacion2 =''
    
    if not(final == 'NP' or final == 'Monte Carlo' or final == 'Final'):
        
        calificacion1 = float(final)
    
        if 6 <= calificacion1 < 6.5:
            calificacion2 = '6 (Seis)'
        elif 6.6 <= calificacion1 < 7.5:
            calificacion2 = '7 (Siete)'
        elif 7.6 <= calificacion1 < 8.5:
            calificacion2 = '8 (Ocho)'
        elif 8.6 <= calificacion1 < 9.5:
            calificacion2 = '9 (Nueve)'
        else:
            calificacion2 = '10 (Diez)'

    return calificacion2

def concatenaNombre(nombres, apellido1, apellido2):
    return nombres + " " + apellido1 + " " + apellido2

def defineSaludo(entrada):
    if entrada == "1":
        return "Alumno"
    else:
        return "Alumna"

def elaboraConstancia(nombreCompleto, numeroCuenta, promedioExamenes, aportaExamenes, \
                      entregaEjercicios, aportaEjercicios, promedio, ajuste, final):
    
    ruta = '2023_1_Cartas/'
    nombre_archivo = nombreCompleto.strip() + '_Detalle_Evaluaciones_Fisica_Computacional.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad Universitaria a 5 de diciembre de 2022.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = nombreCompleto + '. <br/>'\
                        'Número de cuenta: ' + numeroCuenta
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'El peso que le corresponde a los exámenes es de 65/100 y a los ejercicios 35/100, dado que se canceló el proyecto a desarrollar. <br/> A continuación se presenta el detalle de la evaluación para el curso de Física Computacional que cursaste durante el semestre 2023-1.  <br/><br/> Promedio de exámenes: ' + promedioExamenes + '.<br/> Aportación Exámenes: ' + aportaExamenes + '.<br/><br/> Ejercicios entregados: ' + entregaEjercicios + ' de 44 ejercicios.<br/> Aportación ejercicios: ' + aportaEjercicios + '.<br/><br/> Promedio obtenido: ' + promedio + '.<br/><br/>'
    
    if float(promedioExamenes) == 0.:
        ptextomensaje= ptextomensaje + 'Tu calificación del es curso es: <strong>No presentó (NP)</strong>.<br/>'
    
    elif float(promedioExamenes) < 6.:
        ptextomensaje= ptextomensaje + 'Tendrás que presentar Examen Final.<br/>'
    
    elif float(promedioExamenes) > 6.:
        ptextomensaje= ptextomensaje + 'Se aplicó un ajuste con carácter de evaluación formativa a todo el grupo, en tu caso, el ajuste pasa a ser ' + ajuste + '. Se aplica la regla de redondeo para dejar un valor entero, que es la misma para todos.<br/><br/> Tu calificación final del es curso es: <strong>' + final + '</strong>.<br/>'
        
                    
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def readinputdata(filename): 
    fichero=open(filename,'r') 
    f=[] 
    line='0' 
    with open(filename) as csv_file:
        for line in csv.reader(csv_file, delimiter=','): #
            if len(line)>0 : 
                f.append(line) 
    fichero.close() 
    return array(f)


data=readinputdata(r'Grupo_2023_1_Detalle.csv') 
# print (range(1, len(data))) #range(1,26)

for i in range(1, len(data)):
# for i in range(1, 2):
    nombreCompleto = concatenaNombre(data[i][2], data[i][0], data[i][1])
    numeroCuenta = data[i][3]
    promedioExamenes = data[i][4]
    aportaExamenes = data[i][5]
    entregaEjercicios = data[i][6]
    aportaEjercicios = data[i][7]
    promedio = data[i][8]
    ajuste = data[i][9]
    final = data[i][10]
    print(nombreCompleto, calificacionCadena(final))
    elaboraConstancia(nombreCompleto, numeroCuenta, promedioExamenes, \
                      aportaExamenes, entregaEjercicios, aportaEjercicios, \
                      promedio, ajuste, calificacionCadena(final))

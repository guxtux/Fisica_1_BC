#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:14:07 2022

@author: gustavo
"""

import pandas as pd
import hashlib
import os
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY

def cargaArchivo(nombreArchivo):
    datos = pd.read_csv(nombreArchivo, sep = ',', header = 0)
    df = pd.DataFrame(datos)
    return df

def generaCadena(cuenta, nombre):
    cadena = cuenta + nombre
    hashed_string = hashlib.sha256(cadena.encode('utf-8')).hexdigest()
    return hashed_string

def quitaEspacios(cadenaEntrada):
    return cadenaEntrada.replace(" ", "")

def fechaActual(date):
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    dia = date.day
    mes = meses[date.month - 1]
    year = date.year
    cadena = 'Ciudad Universitaria a {0:} de {1:} de {2:}.'.format(dia, mes, year)
    return cadena

def elaboraConstancia(nombreCompleto, numeroCuenta, pTareas, pExamen, promedio, campana, calificacionFinal, comentarios, selloDigital, fecha):
    
    nombrePDF = nombreCompleto.strip() + ' Calificacion_Final_MAF' + '.pdf'
    pathArchivo = 'Cartas/'
    
    pathDocumento = os.path.join(pathArchivo, nombrePDF)
    
    objetoCanvas = Canvas(pathDocumento, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, fecha)
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = nombreCompleto + '. <br/> Número de cuenta: ' + numeroCuenta
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    cadenaCierre = '<br/><br/> Esta calificación se asentará en el acta oficial del curso, una vez que se haya realizado la captura y la firma electrónica, se les notificará vía correo electrónico, por lo que en un par de días ya podrán ver reflejada la calificación en su historial académico. <br/><br/>Atentamente, <br/>M. en C. Ramón Gustavo Contreras Mayén.'
    
    ptextomensaje = 'A continuación se presenta el resumen de la evaluación para el curso de Matemáticas  Avanzadas de la Física que cursaste durante el semestre 2022-2.  <br/><br/>' + \
'Promedio de tareas: ' + pTareas + '<br/> Promedio de exámenes: ' + pExamen + '<br/><br/>' + \
'De acuerdo al esquema de evaluación presentado al inicio del curso, con los promedios obtenidos de los ejercicios y los exámenes, tu promedio del curso es: ' + promedio  + '.<br/><br/>'

    if int(calificacionFinal) == 10:
        ptextomensaje = ptextomensaje + 'La calificación final que obtuviste es: ' + str(calificacionFinal) + '.<br/><br/>' + comentarios + cadenaCierre
    elif (6 <= int(calificacionFinal) < 10):
        ptextomensaje = ptextomensaje + 'Se aplicó un ajuste a la evaluación para todo el grupo, por lo que tu promedio queda en: ' + campana + ', de esta manera, la calificación final que obtuviste es: ' + str(calificacionFinal) + '.<br/><br/>' + comentarios + cadenaCierre
    elif int(calificacionFinal) == 5:
        ptextomensaje = ptextomensaje + 'La calificación final que obtuviste es: ' + str(calificacionFinal) + '.<br/><br/>' + comentarios + cadenaCierre
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    story3 = []
    
    cadenaHash256 = 'Sello digital: ' + selloDigital
    styles.add(ParagraphStyle(name='Sello', alignment=TA_LEFT, fontSize = 12, fontName='Courier', leading=12))
    story3.append(Paragraph(cadenaHash256, styles['Sello']))
    
    frame3 = Frame(50, 10, 6.5*inch, 1*inch, showBoundary=0)
    frame3.addFromList(story3, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def elaboraEvalRubrica(Nombre, Preparacion, T_Experimental, Participacion, Reporte, Conclusiones, Extra, Calificacion, Comentarios):
    
    ruta = '2023_Evaluaciones/Practica_09'
    nombre_archivo = Nombre.strip() + '_Practica_09.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 14 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Nombre + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la evaluación obtenida en tu reporte de la Práctica 9 - Leyes de Newton, en conformidad con la rúbrica que se anunció de manera oportuna, se indica el puntaje obtenido y el total de puntos por la actividad.<br/><br/> Preparación: <u>' + Preparacion + '</u><br/> Trabajo Experimental: <u>' + T_Experimental + '</u><br/> Participación: <u>' + Participacion + '</u><br/> Reporte: <u>' + Reporte + '</u><br/> Conclusiones: <u>' + Conclusiones + '</u><br/> Puntos extra: <u>' + Extra + '</u>'
    
    ptextomensaje = ptextomensaje + '<br/><br/>Calificación:  <u>' + Calificacion + '</u><br/><br/>Comentarios: ' + Comentarios
                        
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def elaboracartaEvalContinua(Nombre, ETP, Componente_Vector, Componente_4_Vectores, Ejercicio_Trabajo, Kepler, O4A, Gravitacion, Puntos, Calificacion):
    
    ruta = '2023_Evaluaciones/EvalContinua'
    nombre_archivo = Nombre.strip() + '_Evaluacion_Continua.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 11 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Nombre + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la relación de ejercicios de evaluación continua que has entregado, así como el puntaje obtenido en cada uno de ellos, el total de puntos considerando que falta una actividad por revisarse (ejercicios del tema de trabajo mecánico), por lo que la calificación obtenida por la evaluación continua, aún es preliminar.<br/><br/> Ecuaciones de tiro parabólico: <u>' + ETP + '/1</u><br/> Componentes de un vector: <u>' + Componente_Vector + '/1</u><br/> Componentes de 4 vectores: <u>' + Componente_4_Vectores + '/1</u><br/> Ordenar 4 aceleraciones: <u>' + O4A + '/1</u><br/> Trabajo de Kepler y elipses: <u>' + Kepler + '/3</u><br/> Ejercicios Gravitación: <u>' + Gravitacion + '/1</u><br/> Ejercicio Trabajo: <u>' + Ejercicio_Trabajo + '/1</u>'
    
    ptextomensaje = ptextomensaje + '<br/><br/>Puntos: <u>' + Puntos + '/9</u><br/> Calificación preliminar: <u>' + Calificacion + '</u><br/>Recuerda que la calificación de evaluación continua, representa el 50 % de la calificación de teoría.'
                        
    ptextomensaje = ptextomensaje + '<br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def elaboracartaConcentrado(Nombre, EC, Examen, Calif_Teoria, Calif_Lab, Final):
    ruta = '2023_Evaluaciones/Concentrado'
    nombre_archivo = Nombre.strip() + '_Evaluacion_Fisica_1.pdf'
    outfilepath = os.path.join( ruta, nombre_archivo )
    objetoCanvas = Canvas(outfilepath, pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 15 de junio de 2023.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = Nombre + '. <br/>'
    
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se te presenta la relación de calificaciones para el TERCER EXAMEN PARCIAL del curso de Física 1, se presentan agrupadas por teoría y laboratorio.<br/><br/><b>Teoría.</b><br/>Evaluación continua: <u>' + EC + '</u><br/> 3er. Examen Parcial: <u>' + Examen + '</u><br/>Calificación de teoría: <u>'+ Calif_Teoria + '</u><br/><br/><b>Laboratorio.</b><br/> Laboratorio <u>' + Calif_Lab + '</u><br/><br/>Recuerda que el 70 % de la calificación del parcial es la calificación de teoría y el otro 30 % es por el Laboratorio.<br/><br/><b>Calificación del TERCER PARCIAL de Física 1: </b> <u>' + Final + '</u>'
    
    ptextomensaje = ptextomensaje + '<br/><br/>Te pido gentilmente me envíes un mensaje por Teams para confirmar que has recibido este documento. Muchas gracias. <br/><br/>Atentamente,<br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()
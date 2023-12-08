# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:02:08 2023

@author: David Guzman

Convierte todos los archivos con extensión .DAT en archivos csv.
Asume que los archivos han sido generados por osciloscopio Tektronix TDS460A,
donde las primeras 4 filas corresponden a: número de datos, resolución 
temporal, dato trigger, y nivel trigger.
Los archivos generados tienen 3 columnas: número de dato, tiempo [s], voltaje [V].
Se almacenan en carpeta /csv_creados/

Probado correctamente 2023-12-07, 5:38pm.
"""

import pandas as pd
import os #para crear directorio
import glob #para buscar archivos en este directorio

##Parámetros para archivo de salida
salida_separador_cols = ";"
salida_separador_decimal = ","

def convierte_archivo(nombre_archivo):
    #extrae todos los datos de voltajes iniciando en fila 4 (header=3). Lo guarda como dataframe de Pandas
    datos_voltaje = pd.read_csv(nombre_archivo, header=3, index_col=False, names=["V"])

    #extrae la resolución temporal de la segunda fila (header=0). Lo guarda como número
    resolucion_temporal = pd.read_csv(nombre_archivo, header=0, index_col=False,nrows=1,names=["delta_t"])
    resolucion_temporal = resolucion_temporal.delta_t[0]
    
    #crea nuevo dataframe con una nueva columna con el tiempo en segundos
    num_datos = len(datos_voltaje)
    tiempos = range(num_datos)*resolucion_temporal
    tiempos = tiempos.round(10) #redondear los valores de tiempo a múltiplos de 0.1ns, pues algunos quedan como 1.999...
    datos_tiempo_voltaje = datos_voltaje #crea una copia del dataframe de voltajes
    datos_tiempo_voltaje["t"]=tiempos #anexa la columna de tiempos, en segundos
    datos_tiempo_voltaje = datos_tiempo_voltaje[["t","V"]] #reordena las columnas
    
    #construye ruta y crea directorio para nuevo archivo
    posicion_punto_archivo = nombre_archivo.rfind(".") #busca última ocurrencia de '.' en la ruta dada
    posicion_separador_directorio = nombre_archivo.rfind("\\") #busca última ocurrencia de '\' en la ruta dada
    ruta_directorio = nombre_archivo[:posicion_separador_directorio] #obtiene ruta hasta antes del directorio final
    ruta_directorio = ruta_directorio + "/csv_creados/" #agrega subcarpeta
    os.makedirs(ruta_directorio, exist_ok=True) #crea directorio, si no existe
    ruta_csv = ruta_directorio + nombre_archivo[posicion_separador_directorio:posicion_punto_archivo]+".csv" #agrega nombre original quitando ".xxxx", agregando ".csv"
    
    #genera nuevo archivo de datos
    datos_tiempo_voltaje.to_csv(ruta_csv,sep=salida_separador_cols,decimal=salida_separador_decimal)
    


#archivos_en_este_directorio = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
archivos_dat_en_este_directorio = glob.glob('./*.dat') #busca archivos con extensión .DAT en directorio actual

for a in archivos_dat_en_este_directorio:
    print('Convirtiendo ' + a)
    convierte_archivo(a)
    
print('Fin rutina.')
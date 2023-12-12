# osciloscopio-Tektronix-TDS460A
Rutinas de manipulación de datos tomados con osciloscopio Tektronix TDS460A.

## convertir_dat_Tektronix_en_csv.py

Convierte todos los archivos con extensión .DAT en archivos csv.
Asume que los archivos han sido generados por osciloscopio Tektronix TDS460A,
donde las primeras 4 filas corresponden a: número de datos, resolución 
temporal, dato trigger, y nivel trigger.
Los archivos generados tienen 3 columnas: número de dato, tiempo [s], voltaje [V].

Crea csv tanto en formato inglés como europeo.

* Inglés:    pi,3.14
* Europeo:   pi;3,14

Se almacenan en carpeta /csv_creados_en/ o en carpeta /csv_creados_eu/.

Probado correctamente 2023-12-07, 5:38pm.

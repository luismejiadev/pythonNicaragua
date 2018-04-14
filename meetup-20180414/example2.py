import os
import pandas as pd
import datetime

# EJEMPLO ARCHIVO 889mil Filas 10 columnas
df = pd.read_csv('/home/luis/Downloads/bAHVKks4JenB7xeMEQom65_20180403164611.csv', low_memory=False)
print df.shape
columns = [
    u'ID Unico',
    u'Fecha y Hora',
    u'Respuesta'
]
df.to_csv('example.csv', columns=columns)

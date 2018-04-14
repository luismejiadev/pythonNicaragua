import os
import pandas as pd
import datetime
from utils import to_excel

# EJEMPLO ARCHIVO 889mil Filas 4 columnas
df = pd.read_csv('example.csv', low_memory=False)
print df.shape
columns = list(df.columns)
print columns
columns[0] = 'user_id'
print columns
df.columns = columns
# print df.head()

result = df.pivot_table(
    values=['user_id'],
    index='ID Unico',
    columns='Respuesta',
    aggfunc=len,
    fill_value=0,
    margins=True
)
print result
to_excel(result, 'por_respuesta', use_index=True)

df['Fecha'] = df['Fecha y Hora'].apply(lambda x: x[:10])
result2 = df.pivot_table(
    values=['user_id'],
    index='ID Unico',
    columns='Fecha',
    aggfunc=len,
    fill_value=0,
    margins=True
)
# to_excel(result2, 'por_fecha', use_index=True)

result3 = df.pivot_table(
    values=['user_id'],
    index=['ID Unico', 'Respuesta'],
    columns='Fecha',
    aggfunc=len,
    fill_value=0,
    margins=True
)
# to_excel(result3, 'por_fecha_y_respuesta', use_index=True)

df['Hora'] = df['Fecha y Hora'].apply(lambda x: x[11:13])
result4 = df.pivot_table(
    values=['user_id'],
    index=['Hora'],
    columns=['Fecha', 'Respuesta'],
    aggfunc=len,
    fill_value=0,
    margins=True
)
to_excel(result4, 'por_fecha_y_hora', use_index=True)

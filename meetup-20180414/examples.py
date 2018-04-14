import os
import pandas as pd
import datetime
from utils import to_excel

sales = [('Jones LLC', 150, 200, 50),
         ('Alpha Co', 200, 210, 90),
         ('Blue Inc', 140, 215, 95)]
labels = ['account', 'Jan', 'Feb', 'Mar']
df = pd.DataFrame.from_records(sales, columns=labels)
to_excel(df, 'array')


sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

df = pd.DataFrame(sales)
to_excel(df, 'array_dict')

sales = [
    ('account', ['Jones LLC', 'Alpha Co', 'Blue Inc']),
    ('Jan', [150, 200, 50]),
    ('Feb', [200, 210, 90]),
    ('Mar', [140, 215, 95]),
]

df = pd.DataFrame.from_items(sales)
to_excel(df, 'tuplas')


sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 50],
         'Feb': [200, 210, 90],
         'Mar': [140, 215, 95]}

df = pd.DataFrame.from_dict(sales)
to_excel(df, 'dict')
to_excel(df, 'dict_columns', ['account', 'Jan', 'Feb', 'Mar'])
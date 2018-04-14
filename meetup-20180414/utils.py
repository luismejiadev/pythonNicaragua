import os
import pandas as pd


def to_excel(df, file_name='simple-report', columns=None, use_index=False):
    file_name += '.xlsx'
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    extra_params = {}
    if columns:
        extra_params['columns'] = columns

    extra_params['index'] = use_index
    df.to_excel(writer, **extra_params)
    writer.save()
    # abrir archivo
    os.popen("libreoffice %s &" % file_name).read()

import pandas as pd

def clean_data(df):
    mail = ['Message']
    for i in mail:
        df[i] = df[i].apply(lambda x : x.replace(',', ' '))
        df[i] = df[i].apply(lambda x: x.replace('!',''))
        df[i] = df[i].apply(lambda x: x.replace('\r\n\r\n',' '))
        df[i] = df[i].apply(lambda x : x.replace('.', ' '))
        df[i] = df[i].apply(lambda x: x.replace('?',' '))
        df[i] = df[i].apply(lambda x: x.replace('/',' '))
    return df
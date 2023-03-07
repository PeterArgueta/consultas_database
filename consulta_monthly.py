import pandas as pd
import json


directory="outputcsv/"
df = pd.read_csv('database.csv', delimiter=',', header=1)
df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%Y')

# convertir la columna FECHA a formato datetime y ordenar el dataframe
df = df.sort_values("FECHA")

# Obtener la fecha más reciente en el dataframe
latest_date = df['FECHA'].max()

# Obtener el primer día del último mes
first_day_of_last_month = latest_date.replace(day=1) - pd.DateOffset(months=1)

# Filtrar los datos para que solo incluyan los del último mes
last_month_data = df[df['FECHA'] >= first_day_of_last_month]

ID=json.load(open('stationsname.txt'))

for k in ID:
    # Pivotear los datos para tener una columna por variable de interés
    merged_data = last_month_data.pivot(index='FECHA', columns='VARIABLE', values=k)

    merged_data.to_csv(f'{directory}{k}.csv')


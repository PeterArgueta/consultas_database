import pandas as pd

df = pd.read_csv('database.csv', delimiter=',', header=1)
df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%Y')

start = '2023-01-01'
end = '2023-01-31'
estacion = 'COBAN'

# Filtrar los datos para el periodo y estación determinados
filtro = (df['FECHA'] >= start) & (df['FECHA'] <= end)
subset = df.loc[filtro, ['FECHA', 'VARIABLE', estacion]]

# Pivotear los datos para tener una columna por variable de interés
merged_data = subset.pivot(index='FECHA', columns='VARIABLE', values=estacion)
#merged_data.columns.name = None  # Eliminar el nombre de la columna de variables

print(merged_data)

#merged_data.to_csv('coban.csv')
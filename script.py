import pandas as pd

# Cargar el archivo Excel
archivo = 'pruebas_p.xlsx'
df = pd.read_excel(archivo)

# Mostrar las primeras filas del DataFrame
print(df.head())

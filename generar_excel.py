import os
import pandas as pd
import csv

file_path = r'' # Cambiar por la ruta de tu archivo
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
folder_path = os.path.join(desktop_path, 'ExcelFiles')

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
df = pd.read_excel(file_path, dtype={'SKU_Base': str})  

for discount, group in df.groupby('Descto'):
    discount_str = discount.strip()
    if not discount_str.endswith('%'):
        discount_str += '%'
    sku_df = group[['SKU_Base']].rename(columns={'SKU_Base': 'stringCode (codigo)'}) # Renombrar columnas en el exxcel
    file_name = os.path.join(folder_path, f'{discount_str}.csv')
    sku_df.to_csv(file_name, index=False, quoting=csv.QUOTE_MINIMAL)
    print(f'Archivo{file_name} generado con éxito en {folder_path}.')


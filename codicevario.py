
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

file_path = "ds/job_recommendation_dataset.csv"
df = pd.read_csv(file_path)
print(f"Dataset caricato: {df.shape[0]:,} righe × {df.shape[1]} colonne")


print(df.head())
print(df.info())


missing = pd.DataFrame({
    'count': df.isnull().sum(),
    'percent': df.isnull().mean() * 100
}).query('count > 0').sort_values('percent', ascending=False)


if missing.empty:
    print('Nessun valore mancante nel dataset!')
else:
    print(f'{len(missing)} colonne con valori mancanti:')
    display(missing.style.bar(subset=['percent'], color='#d65f5f'))


cat_cols = df.select_dtypes(include=['object', 'string']).columns.tolist()
print(f'Colonne categoriche ({len(cat_cols)}): {cat_cols}')


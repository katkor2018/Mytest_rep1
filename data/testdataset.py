import pandas as pd
df = pd.read_csv('Cars Datasets 2025.csv', encoding='utf-16')
print(df.head())
print(df.describe())
print(df.info())

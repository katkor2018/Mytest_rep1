import pandas as pd

df = pd.read_csv('dz.csv')

average_salary = df.groupby('City')['Salary'].mean()

print(average_salary)
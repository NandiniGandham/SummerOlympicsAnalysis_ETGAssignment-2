# -*- coding: utf-8 -*-
"""SummerOlympicAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13_yS1hPXn0x_ZxXBjKA8GmsMZATiXjwL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("summer.csv")

df.head()

df.isnull().sum()

"""##In how many cities summer olympics is held so far"""

len(df['City'].unique())

"""##Which sport is having most number of gold medals so far"""

a=df[df.Medal=='Gold']
data=[]
a['Sport'].unique()
for sport in a['Sport'].unique():
  data.append([sport,len(a[a['Sport'] == sport])])
df1=pd.DataFrame(data,columns = ['Sport','Gold medals'])
print(df1.sort_values(by='Gold medals',ascending=False).head())
df1.sort_values(by='Gold medals', ascending=False).head().plot(x = 'Sport', y = 'Gold medals', kind = 'bar', figsize = (12,5),color='blue')

"""###Which sport is having most number of medals so far"""

print(df.groupby('Sport').count()['Medal'].sort_values(ascending = False).head())
print(df.groupby('Sport').count()['Medal'].sort_values(ascending = False).head().plot(kind='bar',figsize=(12,5),color='blue'))

"""##Which player has won most number of medals"""

print(df.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head())
print(df.groupby('Athlete').count()['Medal'].sort_values(ascending = False).head().plot(kind='bar',figsize=(12,5),color='blue'))

"""##Which player has won most number of gold medals"""

b=df[df.Medal=='Gold']
data=[]
b['Athlete'].unique()
for Athlete in b['Athlete'].unique():
  data.append([Athlete,len(b[b['Athlete'] == Athlete])])
df1=pd.DataFrame(data,columns = ['Athlete','Gold medals'])
print(df1.sort_values(by='Gold medals',ascending=False).head())
df1.sort_values(by='Gold medals', ascending=False).head().plot(x = 'Athlete', y = 'Gold medals', kind = 'bar', figsize = (12,5),color='blue')

"""##In which year India won first gold medal in summer olympics"""

gold_year = st[st['Country'] == 'IND'].sort_values(by = 'Year').head(1)['Year'].item()
txt="India won it's first Gold Medal in Summer Olympics in the year {0}."
print(txt.format(gold_year))

"""##Which event is most popular in terms of number of players"""

print(df.groupby('Event').count()['Athlete'].sort_values(ascending = False).head())
print(df.groupby('Event').count()['Athlete'].sort_values(ascending = False).head().plot(kind='bar',figsize=(12,5),color='blue'))

"""##Which sport is having most female Gold medalists"""

data=[]
for sport in df['Sport'].unique():
  data.append([sport,len(df[(df['Sport']==sport) & (df['Medal']=='Gold') & (df['Gender']=='Women')])])
df2 = pd.DataFrame(data,columns = ['Sport','Female gold medalist'])
df3=df2.sort_values(by='Female gold medalist', ascending=False).head()
print(df3)
df3.plot(x='Sport',y='Female gold medalist',kind='bar',figsize=(12,4),color='blue')
import pandas as pd
import numpy as np
import json


df = pd.read_csv('spotify_songs_top_100.csv')

def format_date(date):
if '.' in date:
a = date.replace('.', ' ').split()
a[-1] = '20' + a[-1]
date = ' '.join(a)
return date

df['Release Date'] = df['Release Date'].apply(format_date)
df['Release Date'] = pd.to_datetime(df['Release Date'])

# 1
for i in range(len(df['Artist'])):
if str(df['Artist'][i]).find('Ed Sheeran') > -1 :
answer = df['Song'][i]
print(answer, sep= '/n')

# 2
x = df['Release Date']

answer = []
for i in x:
st = str(i).replace('Timestamp(', '')
answer.append(st.replace('-', '').split(' ')[0])

answer.sort()
a1 = str(answer[0][:4]+'-'+answer[0][4:6]+'-'+answer[0][6:])
a2 = str(answer[1][:4]+'-'+answer[1][4:6]+'-'+answer[1][6:])
a3 = str(answer[2][:4]+'-'+answer[2][4:6]+'-'+answer[2][6:])


for i in range(len(x)):
st = str(x[i]).replace('Timestamp(', '').replace(')', '').split(' ')[0]
if str(st).find(a1) > -1 or str(st).find(a2) > -1 or str(st).find(a3) > -1:
print(df['Song'][i], end = '\n')

# 3

answer = {}

for i in range(len(df['Artist'])):
answer[df['Artist'][i]] = 0

for i in range(len(df['Artist'])):
answer[df['Artist'][i]] = answer[df['Artist'][i]] + float(str(df['Streams (Billions)'][i]).replace(',',''))


for i in answer:
print('{:<55}'.format(i) + '{:>55}'.format(str(answer[i])))

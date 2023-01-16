import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

df = pd.read_csv('spotify_songs_top_100.csv')

def format_date(date):
if '.' in date:
a = date.replace('.', ' ').split()
a[-1] = '20' + a[-1]
date = ' '.join(a)
return date

df['Release Date'] = df['Release Date'].apply(format_date)
df['Release Date'] = pd.to_datetime(df['Release Date'])

x = df['Release Date']
y = df['Song']

popular_song = {}
for i in range(len(x)):
st = str(x[i]).replace('Timestamp(', '').replace(')', '').split(' ')[0].split('-')[0]
popular_song[st] = 0

for i in range(len(x)):
st = str(x[i]).replace('Timestamp(', '').replace(')', '').split(' ')[0].split('-')[0]
popular_song[st] = popular_song[st]+1

plt.title('Amount of popular songs per year')
myKeys = list(popular_song.keys())
myKeys.sort()
sorted_dict = {i: popular_song[i] for i in myKeys}
plt.xlabel('Years')
plt.ylabel('Amount of songs')
plt.bar(sorted_dict.keys(), list(sorted_dict.values()),color='blue', alpha=0.5)
plt.show()

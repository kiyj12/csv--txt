#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd

for k in range(2003, 2014):
    file = pd.read_excel(r'C:/Users/kiyj1/Documents/LISL/멜론 가사\아이돌 가사 %d.xlsx'%(k), encoding = 'utf-8')
    #file.head()

    lyrics = file['가사']
    singer = file['가수']
    title = file['제목']

    for i in range(0,len(file)):
        with open('아이돌 가사 %d 텍파\%s - %s.txt'%(k, title.iloc[i], singer.iloc[i]), 'w', encoding = 'utf-8') as f:
            f.write(str(lyrics.iloc[i]))


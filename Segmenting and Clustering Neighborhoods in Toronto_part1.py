#!/usr/bin/env python
# coding: utf-8

# ### 1. Download packages that are needed

# In[1]:


#library to handle data in a vectorized manner 
import numpy as np


# In[3]:


#library for data analysis
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#library to handle JSON files
import json

#convert an address into longitude and latitude values
from geopy.geocoders import Nominatim

#library to handle requests
import requests

#transform JSON file into a pandas dataframe
from pandas.io.json import json_normalize 

#Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors 

#import k-means from clustering stage
from sklearn.cluster import KMea

#map rendering library
import folium 

print('Libraries Imported')


# ### 2. Import table from Wikipedia page 

# In[9]:


table_contents=[]
table=soup.find('table')
for row in table.findAll('td'):
    cell = {}
    if row.span.text=='Not assigned':
        pass
    else:
        cell['PostalCode'] = row.p.text[:3]
        cell['Borough'] = (row.span.text).split('(')[0]
        cell['Neighborhood'] = (((((row.span.text).split('(')[1]).strip(')')).replace(' /',',')).replace(')',' ')).strip(' ')
        table_contents.append(cell)

# print(table_contents)
df=pd.DataFrame(table_contents)
df['Borough']=df['Borough'].replace({'Downtown TorontoStn A PO Boxes25 The Esplanade':'Downtown Toronto Stn A',
                                             'East TorontoBusiness reply mail Processing Centre969 Eastern':'East Toronto Business',
                                             'EtobicokeNorthwest':'Etobicoke Northwest','East YorkEast Toronto':'East York/East Toronto',
                                             'MississaugaCanada Post Gateway Processing Centre':'Mississauga'})
df


# In[11]:


df.shape


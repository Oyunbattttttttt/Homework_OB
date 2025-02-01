import pandas as pd 
import re
import numpy as np

# Load the data
main_path = 'input/'
df = pd.read_excel(main_path + 'bz_serg01_imp.xlsx')


df.columns # column names
df.head()  # first 5 rows
df.tail()  # last 5 rows

# Split the data into 3 parts
cols = df.columns
df[cols[:5]]
df[cols[:10]]
df[cols[10:20]]
df[cols[20:30]]
df[cols[30:40]]


df.info() # data types and missing values
df['Чингэлгийн дугаар']
df['Талбай:']


## NA Check for missing values
df.isna()
df.isna().sum() # axis=0
df.isna().sum(axis=1)


# Duplicates
df.duplicated() # if duplicated
df.duplicated().sum() # number of unique duplicates

df.duplicated().
df.columns()



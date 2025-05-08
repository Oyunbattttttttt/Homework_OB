import pandas as pd 
import re
import numpy as np
from datetime import datetime
import os
from openpyxl import load_workbook
pd.options.mode.chained_assignment = None


main_path = '3.unegui/data/202504/'

df1 = pd.read_excel(main_path + 'data1.xlsx', engine='openpyxl')
df2 = pd.read_excel(main_path + 'data2.xlsx', engine='openpyxl')
df3 = pd.read_excel(main_path + 'data3.xlsx', engine='openpyxl')
df4 = pd.read_excel(main_path + 'data4.xlsx', engine='openpyxl')
df5 = pd.read_excel(main_path + 'data5.xlsx', engine='openpyxl')
df6 = pd.read_excel(main_path + 'data6.xlsx', engine='openpyxl')
df7 = pd.read_excel(main_path + 'data7.xlsx', engine='openpyxl')
df8 = pd.read_excel(main_path + 'data8.xlsx', engine='openpyxl')
df9 = pd.read_excel(main_path + 'data9.xlsx', engine='openpyxl')
df10 = pd.read_excel(main_path + 'data10.xlsx', engine='openpyxl')
df11 = pd.read_excel(main_path + 'data11.xlsx', engine='openpyxl')
df12 = pd.read_excel(main_path + 'data12.xlsx', engine='openpyxl')
df13 = pd.read_excel(main_path + 'data13.xlsx', engine='openpyxl')
df14 = pd.read_excel(main_path + 'data14.xlsx', engine='openpyxl')
df15 = pd.read_excel(main_path + 'data15.xlsx', engine='openpyxl')
df16 = pd.read_excel(main_path + 'data16.xlsx', engine='openpyxl')
df17 = pd.read_excel(main_path + 'data17.xlsx', engine='openpyxl')
df18 = pd.read_excel(main_path + 'data18.xlsx', engine='openpyxl')
df19 = pd.read_excel(main_path + 'data19.xlsx', engine='openpyxl')
df20 = pd.read_excel(main_path + 'data20.xlsx', engine='openpyxl')


df = pd.concat([df1, df2,df3, df4 , df5, df6, df7, df8, df9, df10, df11, df12, df13,df14,df15,df16,df17,df18,df19,df20], ignore_index=True)
cols = df.columns

# Duplicates шалгах
df.duplicated() # if duplicated
df.duplicated().sum() # number of unique duplicates

df[df.duplicated()] # duplicated rows
df[df.duplicated()]['id'].value_counts().sum() # duplicated ids


df_dup = df[df.duplicated()] # duplicated rows
df.drop_duplicates(subset=['title', 'id',
       'Мотор багтаамж:', 'Хурдны хайрцаг:', 'Өнгө:',
       'Үйлдвэрлэсэн он:', 'Орж ирсэн он:',
        'Хөтлөгч:', 'Явсан:', 'Хаалга:',
       ], keep='first',inplace=True)

df['id'].duplicated().sum()
df_sort = df.sort_values(by="date_clean", ascending=True)

df_sort.to_excel("3.unegui/data/latest_version.xlsx", index=False)
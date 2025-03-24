import pandas as pd 
import re
import numpy as np
from datetime import datetime
import os
from openpyxl import load_workbook
pd.options.mode.chained_assignment = None


main_path = 'unegui/data/202503/'

df1 = pd.read_excel(main_path + 'data1.xlsx', engine='openpyxl')
df2 = pd.read_excel(main_path + 'data2.xlsx', engine='openpyxl')
df3 = pd.read_excel(main_path + 'data3.xlsx', engine='openpyxl')
df4 = pd.read_excel(main_path + 'data4.xlsx', engine='openpyxl')
df5 = pd.read_excel(main_path + 'data5.xlsx', engine='openpyxl')
df6 = pd.read_excel(main_path + 'data6.xlsx', engine='openpyxl')
df7 = pd.read_excel(main_path + 'data7.xlsx', engine='openpyxl')


df = pd.concat([df1, df2,df3, df4 , df5, df6, df7], ignore_index=True)
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

df.to_excel("unegui/data/output_file1.xlsx", index=False)
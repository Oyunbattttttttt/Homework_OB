import pandas as pd 
import numpy as np
import os 
import re

os.getcwd()
os.chdir('2_Data_cleaning/unegui')

df = pd.read_csv('input/data.csv')

df.columns
df.dtypes

# rename columns

df.columns

df[['Байршил:','location:','location']]

df.isna().sum()

# remove unnecessary columns
df.drop(columns=['Байршил:','location:'], inplace=True)

df.isna().sum()

# with lift na 
df[df['lift'].isna()]['url']
df[df['ad_id'] == 8088508]   # ads posted earlier than Oct, 2024 miss lift

# no text
print(df[df['ad_text'].isna()][['date','ad_text','url','lift']])


# duplicates

df.duplicated().sum()
df_dup = df[df.duplicated()]  # 348
len(df_dup['ad_id'].unique()) # 294
df_dup['ad_id'].value_counts() # 1-3

df_dup[df_dup['ad_id'] == 8763998] # 1
df[df['ad_id'] == 8763998] # 1

df_dup2 = df[df.duplicated(subset=['ad_id','date','time'])] # tot_dup - 1
df_dup2['ad_id'].value_counts() # 1-3
df[df['ad_id'] == 8366690] # 26
df[df['ad_id'] == 8795392] # 1
df[df['ad_id'] == 8505780] # 1


df.drop_duplicates(subset=['ad_id','date','time','price_total'],keep='first',inplace=True)
df_dup3 = df[df.duplicated(subset=['ad_id','date','time'])]
df_dup3['ad_id'].value_counts() # 1-3
df[df['ad_id'] == 8713854] # 1


# area 
df['area'] = df['size'].apply(lambda x: re.findall('\d+[\.\d]*', x)[0]).astype(float)
import re

# Correct the regular expression by using a raw string
df['area'] = df['size'].apply(lambda x: re.findall(r'\d+[\.\d]*', x)[0]).astype(float)


df[['size','area']].dtypes
df['area'].sort_values(ascending=False)

a_int = [0, 10, 50, 100, 400, np.inf]

df['area_int'] = pd.cut(df['area'], bins=a_int, labels=['<10','10-50','50-100','100-400','400+'])
df[['area', 'area_int']]

df['area_int'].value_counts()
df[df['area_int'] == '400+'][['area','url','price_total','ad_id']]

# fix outliers in 400+
df.loc[df['ad_id'] == 8597990, 'area'] = 54


df[df['area_int'] == '<10'][['area','url','price_total','ad_id']]
df.loc[df['ad_id'] == 8781199, 'area'] = 80.88
df.loc[df['ad_id'] == 8781199, 'area']

# remove outliers
df = df[df['area']>10]
df = df[df['area']<400]


# price
df['price_total']
df['price'] = df['price_total'].apply(lambda x: re.findall(r'\d+[\.\d]*', x)[0]).astype(float)
df[['price_total', 'price']]

# terbum
mask = df['price_total'].str.contains('бум', na=False) & (df['price'] < 10)
df.loc[mask, 'price'] = df.loc[mask, 'price'] * 1000
df['mask'] = mask

df[df['mask']==True].sort_values(by='price') 


# interval
p_int = [-np.inf,15,50, 100,200,300,500,1000,5000,np.inf]
df['p_int'] = pd.cut(df['price'], bins=p_int, include_lowest=True)
df[['price','p_int']]
df['p_int'].value_counts().sort_values()

df[df['price'] < 15][['url','price_total','price','p_int']]
df[df['price'] > 4000][['url','price_total','price','p_int']]

df = df[df['price'] < 4000] # remove outliers, price > 4000

# price per m2
df['price_m2'] = df['price']
df[['price','price_m2']]

mask = df['price'] > 15
df.loc[mask, 'price_m2'] = df.loc[mask, 'price'] / df.loc[mask, 'area'] 

df.sort_values(by='price_m2', ascending=False)[['price','price_m2']]


df[df['price_m2'] < 1][['title','url','price_m2','price','area','price_total']]
df[df['price_m2'] > 15][['title','url','price_m2','price','area','price_total']]

# remove outliers
df = df[df['price_m2'] > 1]
df = df[df['price_m2'] < 35]

# df[['date','time','price','area','price_m2','price_total','location']].to_csv(r'D:\economics\repo_later\house_price\map\price_data.csv', encoding='utf-8-sig', index=False)

# location
df_loc = pd.read_csv('input/location.csv')
df = pd.merge(df, df_loc, on='location', how='left')
df[['location','mylocation']]

df_price = df.groupby('mylocation').agg({'price_m2':['median','min','max','count']})
df_price.sort_values(by=('price_m2','count'), ascending=False)
df_price.sort_values(by=('price_m2','median'), ascending=False)

df_price.to_csv('result/price_location.csv', encoding='utf-8-sig')



df_price_dist = df.groupby('district').agg({'price_m2':['median','min','max','count']})


df['room_num']

df.groupby(['district','room_num']).agg({'price_m2':['median','min','max','count']})   

# pivot table district vs room_num
pd.pivot_table(df, values='price_m2', index='district', columns='room_num', aggfunc=['median'])

#Compare the median price per square meter between apartments with and without garage

df.groupby(['district','garage']).agg({'price_m2':['median','count']})  

pd.pivot_table(df, values='price_m2', index='garage', columns='room_num', aggfunc=['median'])

median_price_garage_vs_m2 = df.groupby('garage')['price_m2'].median()
print(median_price_garage_vs_m2)

# Calculate the median price by “floor_at”
median_price_floor_at = df.groupby('floor_at')['price_m2'].median()
print(median_price_floor_at)

# For the ads (identified by ad_id) that were renewed or updated, how long after the initial posting did this occur?
# Udriin zuruug olno

df_dup[['date_collect', 'ad_id','date','url']]
print(df_dup.groupby('ad_id')['date'].count()) #294

df_dup['date'] = pd.to_datetime(df_dup['date'])
date1 = df_dup.groupby(['ad_id', 'url'])['date'].min().reset_index()
date1.rename(columns = {'date': 'date1'}, inplace = True)
date2 = df_dup.groupby(['ad_id', 'url'])['date'].max().reset_index()
date2.rename(columns = {'date': 'date2'}, inplace = True)

df_new = pd.merge(date1, date2, on='ad_id')

df_new['date_zuruu'] = (df_new['date2'] - df_new['date1']).dt.days

df_new.sort_values(by='date_zuruu', ascending=False)
df_new['date_zuruu'].mean()
df_new['date_zuruu'].max()
df_new['date_zuruu'].min()
df_new['date_zuruu'].unique()
print(df_new)


# df_dup = df[df.duplicated()]  # 348
# len(df_dup['ad_id'].unique()) # 294
# df_dup['ad_id'].value_counts() # 1-3

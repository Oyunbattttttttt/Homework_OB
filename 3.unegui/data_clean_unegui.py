import pandas as pd 
import re
import numpy as np
from datetime import datetime
pd.options.mode.chained_assignment = None


main_path = '3.unegui/'
df1 = pd.read_csv(main_path + 'unegui_ads_1.csv')
df2 = pd.read_csv(main_path + 'unegui_ads_2.csv')
df3 = pd.read_csv(main_path + 'unegui_ads_3.csv')
df4 = pd.read_csv(main_path + 'unegui_ads_4.csv')
df5 = pd.read_csv(main_path + 'unegui_ads_5.csv')


df = pd.concat([df1, df2,df3,], ignore_index=True)
cols = df.columns

# Огноо янзлав
df["date"]

def clean_date(val):
    if "Өнөөдөр" in val:
        today_str = datetime.today().strftime("%Y-%m-%d")
        time_part = val.split("Өнөөдөр")[1].strip()  # Extract time
        return f"{today_str} {time_part}"
    elif "Өчигдөр" in val:  # If you have "Yesterday"
        yesterday = datetime.today() - pd.Timedelta(days=1)
        yest_str = yesterday.strftime("%Y-%m-%d")
        time_part = val.split("Өчигдөр")[1].strip()
        return f"{yest_str} {time_part}"
    else:
        return val  # Leave unchanged if not matching

df['date_clean'] = df['date'].apply(clean_date)

df['date_clean'] = df['date_clean'].str.replace("Нийтэлсэн:", "").str.strip()
df['date_clean'] = pd.to_datetime(df['date_clean'], format="%Y-%m-%d %H:%M")

# Үнэ янзлав
df['price']

df['price'] = df['price'].apply(lambda x: re.findall(r'\d+[\.\d]*', x)[0]).astype(float)
df[['price']].dtypes
df.loc[:,'price'] = df['price'] * 1000000

# Машины марк
df['title'] = df['title'].apply(lambda x: x.split(',')[0].strip())

# Явсан км
df['Явсан:'] = df['Явсан:'].str.replace("км", "").str.strip()

# Print
df.to_excel("3.unegui/output_file1.xlsx", index=False)






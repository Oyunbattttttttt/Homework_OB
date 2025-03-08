import pandas as pd 
import re
import numpy as np
pd.options.mode.chained_assignment = None

# Load the data
main_path = 'input/'
df1 = pd.read_excel(main_path + 'serg2023_01_imp.xlsx')
df2 = pd.read_excel(main_path + 'serg2023_02_imp.xlsx')
df3 = pd.read_excel(main_path + 'serg2023_03_imp.xlsx')
df4 = pd.read_excel(main_path + 'serg2023_04_imp.xlsx')
df5 = pd.read_excel(main_path + 'serg2023_05_imp.xlsx')
df6 = pd.read_excel(main_path + 'serg2023_06_imp.xlsx')
df7 = pd.read_excel(main_path + 'serg2023_09_imp.xlsx')
df8 = pd.read_excel(main_path + 'serg2023_10_imp.xlsx')
df9 = pd.read_excel(main_path + 'serg2023_11_1imp.xlsx')
df10 = pd.read_excel(main_path + 'serg2023_12_imp.xlsx')
df11 = pd.read_excel(main_path + 'serg_imp07_1.xlsx')
df12 = pd.read_excel(main_path + 'serg_imp07_2.xlsx')
df13 = pd.read_excel(main_path + 'serg_imp07_3.xlsx')
df14 = pd.read_excel(main_path + 'serg_imp08_1.xlsx')
df15 = pd.read_excel(main_path + 'serg_imp08_2.xlsx')
df16 = pd.read_excel(main_path + 'serg_imp08_3.xlsx')

# Merge the data
df = pd.concat([df1, df2, df3, df4, df5 ,df6 ,df7 ,df8 ,df9 ,df10 ,df11 ,df12 ,df13 ,df14 ,df15 ,df16], ignore_index=True)
df["date_column"] = pd.to_datetime(df["Огноо"], format="%d-%b-%y")

df.columns # column names
df.head()  # first 5 rows
df.tail()  # last 5 rows

# Split the data into 3 parts
cols = df.columns
cols1 = df_cleaned_1.columns
df.info() # data types and missing values
## NA Check for missing values
df.isna()
df.isna().sum() # axis=0
df.isna().sum(axis=1)

# Duplicates
# Барааны төрлөөр давхардсан мэдээллийг устгах
df_cleaned = df.drop_duplicates(subset=['Тээв.х.дугаар', 'Тээврийн төрөл','Нэр','Огноо', 'Чингэлэг' ,'Илгээгч',],keep='first')

# Display the result
print(df_cleaned)

# Хөдөлгөөнт бус тээврийн хэрэгслийг устгав

df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Хөдөлтгөөнт бус тээвэр']
df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Хөдөлтгөөнт бус тээвэр']
df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Бусад тээврийн хэрэгсэл']
df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Бусад тээврийн хэрэгсэл']
df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Буухиа шуудан']



# Барааны кодоор filter хийх алхам бэлтгэв
# Бинзен код түүж устгав
df_cleaned_1.loc[:, 'Len_1'] = df_cleaned_1['Бараа код'].astype(str).str[:5]
df_cleaned_1 = df_cleaned_1[df_cleaned_1['Len_1'] != '27101'] # бинзен устгав
df_cleaned_1 = df_cleaned_1[df_cleaned_1['Len_1'] != '86090'] # Чингэлэг устгав
df_cleaned_1 = df_cleaned_1[df_cleaned_1['Len_1'] != '86069'] # Вагон устгав

# Чингэлгийн дугаар дээрх 00-г ялгав
df_cleaned_1['Чингэлэг'] = df_cleaned_1['Чингэлэг'].replace("00", np.nan)
df_cleaned_1['Чингэлэг'] = df_cleaned_1['Чингэлэг'].replace("0", np.nan)

df_cleaned_1['Тээв.х.дугаар'] = df_cleaned_1['Тээв.х.дугаар'].replace("00", np.nan)
df_cleaned_1['Тээв.х.дугаар'] = df_cleaned_1['Тээв.х.дугаар'].replace("0", np.nan)

## chingelgiin dugaartai 11s uur bol WGN

# Агаар ялгав

df_cleaned_1.loc[
    (df_cleaned_1['Тээврийн төрөл'].astype(str) == "Агаар"),
    'Тээврийн төрөл_01'
] = 'AIR'
# multimodel ялгав 

df_cleaned_1.loc[
    (df_cleaned_1['Тээврийн төрөл'].astype(str) == "Усан зам"),
    'Тээврийн төрөл_01'
] = 'Multimodel'

# Чингэлгийн дугаар дээр AIR болон FCL -г ялгав. /Zasah/ AIR wagon bolgoh
df_cleaned_1.loc[df_cleaned_1['Чингэлэг'].astype(str).str.len() >= 11, 'Тээврийн төрөл_01'] = 'FCL'

# Тээврийн хэрэгслийн дугаараар FTl -г ялгав
df_cleaned_1.loc[
    (df_cleaned_1['Тээв.х.дугаар'].astype(str).str.len() <= 7) & 
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'FTL'

# FCL LCL ялгав

df_cleaned_1['count_Чингэлгийн дугаар'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Тээврийн төрөл_01', 'Чингэлэг']
)['Чингэлэг'].transform('count')

df_cleaned_1['count_Тээврийн төрөл_01'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Тээврийн төрөл_01', 'Чингэлэг']
)['Тээврийн төрөл_01'].transform('count')

df_cleaned_1['count_Хүлээн авагч'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Нэр', 'Чингэлэг']
)['Нэр'].transform('count')

df_cleaned_1['count_Зөвшөөрсөн/ Татгалзсан огноо'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), "Огноо", 'Чингэлэг']
)["Огноо"].transform('count')

# Тус филтэрүүдээс үлдсэнг шахав
# WGN -г ялгав
df_cleaned_1.loc[
    (df_cleaned_1['Тээврийн төрөл'].astype(str) == "Төмөр зам") & 
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'WGN'

df_cleaned_1.loc[
    (df_cleaned_1['Тээврийн төрөл'].astype(str) == "Авто зам") & 
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'FTL'

# Тээврийн төрөл 2 баган үүсгэв
df_cleaned_1.loc[
    ((df_cleaned_1['count_Чингэлгийн дугаар'] >= 2)) & 
    (df_cleaned_1['Тээврийн төрөл_01'] == "FCL"),
    'Тээврийн төрөл_2'
] = 'LCL'
df_cleaned_1['Тээврийн төрөл_2'].fillna('', inplace=True)

# FTL LTL ялгав

df_cleaned_1['LTL_count_Тээв.х.дугаар'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Тээврийн төрөл_01', 'Тээв.х.дугаар']
)['Тээв.х.дугаар'].transform('count')

df_cleaned_1['LTL_count_Тээврийн төрөл_01'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Тээврийн төрөл_01', 'Тээв.х.дугаар']
)['Тээврийн төрөл_01'].transform('count')

df_cleaned_1['LTL_count_Хүлээн авагч'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Нэр', 'Тээв.х.дугаар']
)['Нэр'].transform('count')

df_cleaned_1['LTL_count_Зөвшөөрсөн/ Татгалзсан огноо'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), "Огноо", 'Тээв.х.дугаар']
)["Огноо"].transform('count')

df_cleaned_1.loc[
    ((df_cleaned_1['LTL_count_Тээв.х.дугаар'] >= 2)) & 
    ((df_cleaned_1['LTL_count_Зөвшөөрсөн/ Татгалзсан огноо'] >= 2)) &
    ((df_cleaned_1['Илгээгч'].astype(str) == "БНХАУ")) &
    (df_cleaned_1['Тээврийн төрөл_01'] == "FTL"),
    'Тээврийн төрөл_2'
] = 'LTL'
df_cleaned_1['Тээврийн төрөл_2'].fillna('', inplace=True)

df_cleaned_1.loc[
    ((df_cleaned_1['LTL_count_Тээв.х.дугаар'] >= 4)) & 
    ((df_cleaned_1['Илгээгч'].astype(str) == "БНХАУ")) &
    (df_cleaned_1['Тээврийн төрөл_01'] == "FTL"),
    'Тээврийн төрөл_2'
] = 'LTL'
df_cleaned_1['Тээврийн төрөл_2'].fillna('', inplace=True)

df_cleaned_1.loc[
    ((df_cleaned_1['LTL_count_Тээв.х.дугаар'] >= 3)) & 
    ((df_cleaned_1['Илгээгч'].astype(str) == "Орос")) &
    (df_cleaned_1['Тээврийн төрөл_01'] == "FTL"),
    'Тээврийн төрөл_2'
] = 'LTL'
df_cleaned_1['Тээврийн төрөл_2'].fillna('', inplace=True)

df_cleaned_1.loc[
    ((df_cleaned_1['LTL_count_Тээв.х.дугаар'] >= 2)) & 
    ((df_cleaned_1['Илгээгч'].astype(str) != "Орос , БНХАУ")) &
    (df_cleaned_1['Тээврийн төрөл_01'] == "FTL"),
    'Тээврийн төрөл_2'
] = 'LTL'
df_cleaned_1['Тээврийн төрөл_2'].fillna('', inplace=True)

df_cleaned_1['Тээврийн төрөл_2'].replace('', np.nan, inplace=True)

# Тээврийн төрөл 2 дээр байгаа хоосон утгуудад 1-г авав
df_cleaned_1['Тээврийн төрөл_2'].fillna(df_cleaned_1['Тээврийн төрөл_01'], inplace=True)

# Хувь хүн компани салгав
df_cleaned_1.loc[df_cleaned_1['Регистр'].astype(str).str.len() == 7, 'Хувь/Байгууллага'] = 'Байгууллага'
df_cleaned_1['Хувь/Байгууллага'].fillna('Хувь хүн', inplace=True)

# Хуучин авто машиг ялгав
df_cleaned_1.loc[df_cleaned_1['Len_1'] == '87034', 'Автомашин эсэх'] = 'Тийм'
df_cleaned_1['Автомашин эсэх'].fillna('Үгүй', inplace=True)

# Export хийх датаг багасгав

df_last = df_cleaned_1.loc[:, ['date_column','Регистр','Нэр','Хувь/Байгууллага','Бараа нэр','Тээврийн төрөл_2',"Мэдүүлэгч","Илгээгч",'Автомашин эсэх','гадаад нэр','Нэгж','Тоо','ГХН',]]


# excel export
df_last.to_excel("output_file.xlsx", index=False)
df_cleaned_1.to_excel("output_file1.xlsx", index=False)





# pivot dataframe 

df_pivot = df.pivot(index='Date', columns='Product', values='Sales')
df.pivot_table(index='Date', columns='Product', values='Sales', aggfunc='sum')


# 2 data frame 1 excel 
# Create an Excel writer object
with pd.ExcelWriter("output.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)  # Export df1 to "Sheet1"
    df2.to_excel(writer, sheet_name="Sheet2", index=False)  # Export df2 to "Sheet2"

print("Excel file created successfully!")


################################################
df_cleaned_1.loc[
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'FTL'

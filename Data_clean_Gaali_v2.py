import pandas as pd 
import re
import numpy as np
pd.options.mode.chained_assignment = None



# Load the data
main_path = 'input/'
df1 = pd.read_excel(main_path + 'bz_serg01_imp.xlsx')
df2 = pd.read_excel(main_path + 'bz_serg02_imp.xlsx')
df3 = pd.read_excel(main_path + 'bz_serg03_imp.xlsx')

# Merge the data
df = pd.concat([df1, df2, df3], ignore_index=True)
df["date_column"] = pd.to_datetime(df["Зөвшөөрсөн/ Татгалзсан огноо"], format="%d-%b-%y")

df.columns # column names
df.head()  # first 5 rows
df.tail()  # last 5 rows

# Split the data into 3 parts
cols = df.columns
df[cols[:5]]
df[cols[:10]]
df[cols[10:20]]
df[cols[20:30]]

df_cleaned_1[cols[50:60]]


df.info() # data types and missing values
df['Чингэлгийн дугаар']
df['Тээврийн төрөл']


## NA Check for missing values
df.isna()
df.isna().sum() # axis=0
df.isna().sum(axis=1)


# Duplicates
# Барааны төрлөөр давхардсан мэдээллийг устгах
df_cleaned = df.drop_duplicates(subset=['Хил дээрх тээврийн хэрэгсэл', 'Тээврийн төрөл','Хүлээн авагч','Зөвшөөрсөн/ Татгалзсан огноо', 'Чингэлгийн дугаар' ,'Илгээгч улс',],keep='first')

# Display the result
print(df_cleaned)

# Хөдөлгөөнт бус тээврийн хэрэгслийг устгав

df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Хөдөлтгөөнт бус тээвэр']

# Барааны кодоор filter хийх алхам бэлтгэв
# Бинзен код түүв
df_cleaned_1.loc[:, 'Len_1'] = df_cleaned_1['Барааны код'].astype(str).str[:5]

# Чингэлгийн дугаар дээрх 00-г ялгав
df_cleaned_1['Чингэлгийн дугаар'] = df_cleaned_1['Чингэлгийн дугаар'].replace("00", np.nan)
df_cleaned_1['Чингэлгийн дугаар'] = df_cleaned_1['Чингэлгийн дугаар'].replace("0", np.nan)
# Чингэлгийн дугаар дээр AIR болон FCL -г ялгав.
df_cleaned_1.loc[df_cleaned_1['Чингэлгийн дугаар'].astype(str).str.len() >= 11, 'Тээврийн төрөл_01'] = 'FCL'

df_cleaned_1.loc[
    (df_cleaned_1['Чингэлгийн дугаар'].astype(str).str.len() == 8) &
    (df_cleaned_1['Len_1'].astype(str) != "27101"),
    'Тээврийн төрөл_01'
] = 'AIR'

# Тээврийн хэрэгслийн дугаараар FTl -г ялгав
df_cleaned_1.loc[
    (df_cleaned_1['Хил дээрх тээврийн хэрэгсэл'].astype(str).str.len() <= 7) & 
    (df_cleaned_1['Len_1'].astype(str) != "27101") &
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'FTL'

df_cleaned_1.loc[
    (df_cleaned_1['Хил дээрх тээврийн хэрэгсэл'].astype(str).str.len() >= 9) & 
    (df_cleaned_1['Len_1'].astype(str) != "27101") &
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'FTL'

df_cleaned_1.loc[
    (df_cleaned_1['Хил дээрх тээврийн хэрэгсэл'].astype(str).str.len() == 8) & 
    (df_cleaned_1['Гарал үүсэл'].astype(str) == "ОХУ") &
    (df_cleaned_1['Len_1'].astype(str) == "27101") &
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'WGN'

df_cleaned_1.loc[
    (df_cleaned_1['Гарал үүсэл'].astype(str) == "ОХУ") &
    (df_cleaned_1['Len_1'].astype(str) == "27101") &
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'WGN'

df_cleaned_1.loc[
    (df_cleaned_1['Тээврийн төрөл_01'].isna()), 
    'Тээврийн төрөл_01'
] = 'FTL'

# FCL ялгав


df_cleaned_1['count_Чингэлгийн дугаар'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Тээврийн төрөл_01', 'Чингэлгийн дугаар']
)['Чингэлгийн дугаар'].transform('count')

df_cleaned_1['count_Тээврийн төрөл_01'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Тээврийн төрөл_01', 'Чингэлгийн дугаар']
)['Тээврийн төрөл_01'].transform('count')

df_cleaned_1['count_Хүлээн авагч'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), 'Хүлээн авагч', 'Чингэлгийн дугаар']
)['Хүлээн авагч'].transform('count')

df_cleaned_1['count_Зөвшөөрсөн/ Татгалзсан огноо'] = df_cleaned_1.groupby(
    [df_cleaned_1['date_column'].dt.to_period('M'), "Зөвшөөрсөн/ Татгалзсан огноо", 'Чингэлгийн дугаар']
)["Зөвшөөрсөн/ Татгалзсан огноо"].transform('count')

# Тээврийн төрөл FCL болон Date column 2 сард 1-с дээш орсон бол LCL гэж ялгав

df_cleaned_1.loc[
    ((df_cleaned_1['count_Чингэлгийн дугаар'] >= 2)) & 
    ((df_cleaned_1['count_Тээврийн төрөл_01'] >= 2)) &
    ((df_cleaned_1['count_Зөвшөөрсөн/ Татгалзсан огноо'] >= 2)) &
    (df_cleaned_1['Тээврийн төрөл_01'] == "FCL"),
    'Тээврийн төрөл_2'
] = 'LCL'
df_cleaned_1['Тээврийн төрөл_2'].fillna('', inplace=True)

df_cleaned_1['count_Чингэлгийн дугаар']
df_cleaned_1['count_Тээврийн төрөл_01']
df_cleaned_1['count_Зөвшөөрсөн/ Татгалзсан огноо']

# pivot dataframe 

df_pivot = df.pivot(index='Date', columns='Product', values='Sales')
df.pivot_table(index='Date', columns='Product', values='Sales', aggfunc='sum')


# 2 data frame 1 excel 
# Create an Excel writer object
with pd.ExcelWriter("output.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Sheet1", index=False)  # Export df1 to "Sheet1"
    df2.to_excel(writer, sheet_name="Sheet2", index=False)  # Export df2 to "Sheet2"

print("Excel file created successfully!")

# Чингэлэг дугаартай бол FCL болон LCL түр ангилруу хийх
# - Duplicate -  Ner , on sar , ilgeegch , Uls ,Teewrin turul ,Teewriin heregsel
# - Hudulguunt bus teewer ustgah /litsenz/

#- Teewrin turluu oloh
# - Agaarin teewriig salgah /teewriin turluus/ nislegin dugartaig
# - Chingeleg dugartai bol FCL LCL tur angilal
#- Uldsengees awtin dugartaig LTL FTL /oros mashinuu dugaar ur bdag/
#- Angilalgui bol orj irsen gaalin baiguullagin codoor huun zamiin uudes busdig ftl ltl angilalruu hiih
#-  1 chingeleg tuhain sard 2 haritlsagch tai import hiigdsen bol tuuwer/ustgalt hiigdeh/
#- busad tohioldold buten chingeleg/ustgalt/w

#Uldegdel
#- dizel tulshig tusdan baraanii kodoor yalgan wagon talbart
#- +huluuruu orj irj bga mashin
#- 


# excel export
df_cleaned_1.to_excel("output_file.xlsx", index=False)

BEAU5373832
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
df['Тээврийн төрөл']


## NA Check for missing values
df.isna()
df.isna().sum() # axis=0
df.isna().sum(axis=1)


# Duplicates
# Барааны төрлөөр давхардсан мэдээллийг устгах
df_cleaned = df.drop_duplicates(subset=['Хил дээрх тээврийн хэрэгсэл', 'Тээврийн төрөл','Хүлээн авагч','Зөвшөөрсөн/ Татгалзсан огноо', 'Чингэлгийн дугаар' ,'Илгээгч улс','Мэдүүлсэн огноо'],keep='first')

# Display the result
print(df_cleaned)

# Хөдөлгөөнт бус тээврийн хэрэгслийг устгав

df_cleaned_1 = df_cleaned[df_cleaned['Тээврийн төрөл'] != 'Хөдөлтгөөнт бус тээвэр']
df_cleaned_1['Тээврийн төрөл']
df_cleaned_1['Тээврийн төрөл'].unique()
df_cleaned_1['Хил дээрх тээврийн хэрэгсэл'].unique()
df_cleaned_1['Чингэлгийн дугаар'].unique()
print(df_cleaned_1)

df_cleaned_1.loc[df_cleaned_1['Чингэлгийн дугаар'].astype(str).str.len() >= 11, 'Тээврийн төрөл_01'] = 'FCL'
df_cleaned_1.loc[df_cleaned_1['Чингэлгийн дугаар'].astype(str).str.len() == 8, 'Тээврийн төрөл_01'] = 'AIR'

df_cleaned_1['Тээврийн төрөл_01'].unique()




# Чингэлэг дугаартай бол FCL болон LCL түр ангилруу хийх
# - Duplicate -  Ner , on sar , ilgeegch , Uls ,Teewrin turul ,Teewriin heregsel
# - Hudulguunt bus teewer ustgah /litsenz/

#- Teewrin turluu oloh
# - Agaarin teewriig salgah /teewriin turluus/ nislegin dugartaig
# - Chingeleg dugartai bol FCL LCL tur angilal
#- Uldsengees awtin dugartaig LTL FTL /oros mashinuu dugaar ur bdag/
#- Angilalgui bol orj irsen gaalin baiguullagin codoor huun zamiin uudes busdig ftl ltl angilalruu hiih
#-  1 chingeleg tuhain sard 2 haritlsagch tai import hiigdsen bol tuuwer/ustgalt hiigdeh/
#- busad tohioldold buten chingeleg/ustgalt/

#Uldegdel
#- dizel tulshig tusdan baraanii kodoor yalgan wagon talbart
#- +huluuruu orj irj bga mashin
#- 


# excel export
df_cleaned_1.to_excel("output_file.xlsx", index=False)
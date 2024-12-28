# Даалгавар 2.1 loop үүсгэв
# loop-р 
for i in range(100):
    print(i)

a = " 1 - 100 ийн хоорондох жагсаалт-c "
b = "хүн"
num = (i)
a + str(num) + " "+ b

# list-р
my_range = range(1,101)
my_range_as_list = list(my_range)
print(list(my_range))

# slice
my_range[2]

a = " 1 - 100 ийн хоорондох жагсаалт "
num = (my_range[2])
a + str(num)

# Даалгавар 2.3
import numpy as np

rng = np.arange(0,100,5)


# Даалгавар 3
# "2024/12/15" string-г datetime хөрвүүлэх

import datetime

datetime.datetime.strptime('2024/12/15', '%Y/%m/%d')
my_date = datetime.datetime.strptime('2024/12/15', '%Y/%m/%d')
new_date = my_date + datetime.timedelta(days=7)

new_date.strftime("%m/%d/%Y")


# даавгавар 4 

# NUMPY СУДЛАХ
A = float()
K = float()
L = float()

f = A*(K**0.3)*(L**0.7)


# Даалгавар 5 dictionary

a_dict = {"ner": "bat"}
bat_dict = {"ner": "bat", "huis": "er", "tsalin": 2500000 ,"tursun ognoo": 2000/10/31}

b_dict = {"ner": "bold"}
bold_dict = {"ner": "bold", "huis": "er", "tsalin": 2800000 ,"tursun ognoo": 2002/10/31}

c_dict = {"ner": "dondog"}
dondog_dict = {"ner": "dondog", "huis": "er", "tsalin": 2000000 ,"tursun ognoo": 2003/10/31}

d_dict = {"ner": "dulam"}
dulam_dict = {"ner": "dulam", "huis": "em", "tsalin": 2500000 ,"tursun ognoo": 2006/10/31}

e_dict = {"ner": "tsetseg"}
tsetseg_dict = {"ner": "tsetseg", "huis": "em", "tsalin": 2600000 ,"tursun ognoo": 2005/10/31}

customer_dict ={"1": bat_dict,"2": bold_dict,"3": dondog_dict,"4": dulam_dict,"5": tsetseg_dict}



customer_dict.keys()

import pandas as pd


datadict = {'ner':["bat" ,"bold" ,"dondog", "dulam", "tsetseg"] ,'huis':["er" ,"er" ,"er", "em", "em"] ,'tsalin':["2500000" ,"2800000" ,"2000000", "2500000", "2600000"] ,'tursun ognoo':["2000/10/31" ,"2002/10/31" ,"2003/10/31", "2006/10/31", "2005/10/31"]}


datadict = {
    'ner':["bat" ,"bold" ,"dondog", "dulam", "tsetseg"] ,
    'huis':["er" ,"er" ,"er", "em", "em"] ,
    'tsalin':["2500000" ,"2800000" ,"2000000", "2500000", "2600000"] ,
    'tursun ognoo':["2000/10/31" ,"2002/10/31" ,"2003/10/31", "2006/10/31", "2005/10/31"]
    }

df = pd.DataFrame(datadict)

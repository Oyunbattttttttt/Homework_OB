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

# Даалгавар 5 dictionary
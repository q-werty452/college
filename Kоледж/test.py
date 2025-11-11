# Задача 1 
my_str = "wdscjfwd6ehrhehf56jhfnnv576"
nums = [int(i) for i in my_str if i.isdigit()]
print(nums)



##############################

import re # Регулярные выражения
my_str = "wdscjfwd6ehrhehf56jhfnnv576"
nums = re.findall("[0-9]+", my_str)
numbers = []
for i in nums:
    numbers.append(int(i))
print(numbers)


##############################


nums = []
tem = ""
for i in my_str:
    if i.isdigit():
        tem += i
    else:
        if tem != "":
            nums.append(int(tem))
            tem = ""
if tem :
    nums.append(int(tem))
print(nums)
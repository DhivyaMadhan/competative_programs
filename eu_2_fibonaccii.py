# -*- coding: utf-8 -*-
# @Time    : 20/01/23
# @Author  : Madhan Kumar S
# @Email   : madhan.ks@logically.co.uk
num_1, num_2 = eval(input("Enter 2 value separated by comma : "))
limit = eval(input("fibonacci sequence: "))
# print(num_1,num_2)
style = [num_1,num_2]
for test in range(0, limit):
    num_3 = num_1 + num_2
    if num_3 >= limit:
        print(f"last iterated index: {test}")
        break
    num_1 = num_2
    num_2 = num_3
    # print(num_3)
    style.append(num_3)
# print(style)
output = 0
for iterate in style:
    if iterate%2 == 0:
        # print(iterate)
        output = output + iterate
print("sum of even fibonacci sequence sum of even fibonacci sequence sum of even fibonacci sequence sum of even fibonacci sequence: ",output)








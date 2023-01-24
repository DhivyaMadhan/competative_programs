# -*- coding: utf-8 -*-
# @Time    : 20/01/23
# @Author  : Madhan Kumar S
# @Email   : madhan.ks@logically.co.uk

result = list()
limit = 1000
for iterate in range(1,1001):
    multiply_by_3 = iterate * 3
    multiply_by_5 = iterate * 5
    if (multiply_by_3 >= limit) & (multiply_by_5 >= limit):
        break
    # print(f"{iterate} * {3} = {output}")
    # print(output)
    result.append(multiply_by_3)
    if multiply_by_5 < limit:
        result.append(multiply_by_5)
print(result)
output1 = 0
for iterate1 in result:
    output1 = output1 + iterate1
# print(output1)

enumerate_result = ""
for index, value in enumerate(result):
    # print(index, value)
    if index == 0:
        enumerate_result = result[index]
    else:
        enumerate_result = enumerate_result + result[index]
print(enumerate_result)

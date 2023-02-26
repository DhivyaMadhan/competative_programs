"""
Website - projecteuler
URL - https://projecteuler.net/problem=1
Question - 001
Notes: natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
result = list()
limit = 10
for iterate in range(1,limit+1):
    multiply_by_3 = iterate * 3
    multiply_by_5 = iterate * 5
    if (multiply_by_3 >= limit) & (multiply_by_5 >= limit):
        break
    # print(f"{iterate} * {3} = {output}")
    # print(output)
    result.append(multiply_by_3)
    # here multiple_by_5 condition finish before multiple_by_3
    if multiply_by_5 < limit:
        result.append(multiply_by_5)
print(result)
output1 = 0
for iterate1 in result:
    output1 = output1 + iterate1
print(output1)

# here it is used as list format

# enumerate_result = ""
# for index, value in enumerate(result):
#     # print(index, value)
#     if index == 0:
#         enumerate_result = result[index]
#     else:
#         enumerate_result = enumerate_result + result[index]
# print(enumerate_result)

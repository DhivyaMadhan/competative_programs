"""
Website - projecteuler
URL - https://projecteuler.net/problem=5
Question - 005
Notes:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

higher_range = 15
smallest_num = list()
for number in range(higher_range*2, 100000*100000):
    flag = True
    for iterate in range(1, higher_range):
        if number % iterate != 0:
            flag = False
            break
    if flag:
        print(number)
        # smallest_num.append(number)
        break
# print(smallest_num)
# print(min(smallest_num))




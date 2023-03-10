"""
Website - projecteuler
URL - https://projecteuler.net/problem=6
Question - 006
Notes: The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum..
"""
import sys
value = sys.argv[1]
# value = 100
list_1 = list()
list_2 = list()
output = 0
sum_of_square = 0
square_of_sum = 0
for iterate in range(1, int(value)+1):
    list_1.append(iterate **2)
    sum_of_square = sum(list_1)
    # print("sum of square:", sum_of_square)
    list_2.append(iterate)
    square_of_sum = sum(list_2)
    square_of_sum = square_of_sum**2
    # print("square of sum:",square_of_sum)
    differance = sum_of_square - square_of_sum
    output = abs(differance)
# print(output)
print("sum of square:", sum_of_square)
print("square of sum:", square_of_sum)
print("Difference between the sum of the squares and the square of the sum:",output)


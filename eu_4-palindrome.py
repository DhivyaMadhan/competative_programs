"""
Website - projecteuler
URL - https://projecteuler.net/problem=4
Question - 004
Notes:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
largest = 0
dummy1, dummy2 = "", ""
largest_mul = [0]*2 #largest_mul = [0, 0]
for iterate in range(100, 200):
    for iterate_1 in reversed(range(100, 999)):
        output = iterate * iterate_1
        # print(output)
        list_value = list(str(output))
        list_value.reverse()
        if list_value == list(str(output)):
            # print(f"{iterate} * {iterate_1} = {output}")
            if (output > largest):
                largest = output
                largest_mul[0] = iterate
                dummy1 = iterate
                largest_mul[1] = iterate_1
                dummy2 = iterate_1
print(f"{largest_mul[0]} * {largest_mul[1]} = {largest}")
print(f"{dummy1} * {dummy2} = {largest}")









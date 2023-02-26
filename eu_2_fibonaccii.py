"""
Website - projecteuler
URL - https://projecteuler.net/problem=2
Question - 002
Notes:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
num_1, num_2 = eval(input("Enter 2 value separated by comma : "))
limit = eval(input("fibonacci sequence limit: "))
# print(num_1,num_2)
fibonacci_series = [num_1, num_2]
for num_of_sequence in range(1, limit):
    num_3 = num_1 + num_2
    if num_3 >= limit:
        print(f"last iterated index: {num_of_sequence}")
        break
    num_1 = num_2
    num_2 = num_3
    # num_1, num_2 = num_2, num_3
    # print(num_3)
    fibonacci_series.append(num_3)
print(fibonacci_series)
output = 0
for iterate in fibonacci_series:
    if iterate % 2 == 0:
        # print(iterate)
        output = output + iterate
print("sum of even fibonacci sequence: ",output)








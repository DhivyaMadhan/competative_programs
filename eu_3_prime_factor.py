"""
Website - projecteuler
URL - https://projecteuler.net/problem=3
Question - 003
Notes:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
value = 150
factor_list, prime_list, not_prime_list = list(), list(), list()
# Here the value of factor can be half of the value ,it can't exceed value/2
for each_iterate in range(2, int(value/2)):
    if value % each_iterate == 0:
        factor_list.append(each_iterate)
print(factor_list)
for input_value in factor_list:
    flag = True
    for prime_factor in range(2, input_value):
        if input_value % prime_factor == 0:
            flag = False
            break
    if flag:
        prime_list.append(input_value)
        print(f"{input_value} is Prime number")
    else:
        not_prime_list.append(input_value)
        # print(f"{input_value} is not a prime number")
print(max(prime_list))
# print(not_prime_list)






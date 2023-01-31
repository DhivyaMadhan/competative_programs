value = 1588477
factor_list, prime_list, not_prime_list = list(), list(), list()
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
        # print(f"{input_value} is Prime number")
    else:
        not_prime_list.append(input_value)
        # print(f"{input_value} is not a prime number")
print(max(prime_list))
# print(not_prime_list)






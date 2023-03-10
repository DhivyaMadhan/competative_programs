"""
Website - projecteuler
URL - https://projecteuler.net/problem=10
Question - 010
Notes:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
"""n = 2000000
prime_number = list()
for each in range(2, n+1):
    flag = True
    for value in range(2, each):
        if each % value == 0:
            flag = False
            break
    if flag:
        prime_number.append(each)
print(prime_number)
# print(count)
sum_of_prime_number = sum(prime_number)
print(f"sum of all the primes below {n}: {sum_of_prime_number}")"""


hi = 10

# create a set excluding even numbers
numbers = set(range(3, hi + 1, 2))
for number in range(3, int(hi ** 0.5) + 1):
    if number not in numbers:
        #number must have been removed because it has a prime factor
        continue

    num = number
    while num < hi:
        print(num)
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print(2 + sum(numbers))


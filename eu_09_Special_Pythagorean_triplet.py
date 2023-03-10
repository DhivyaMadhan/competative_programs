"""
Website - projecteuler
URL - https://projecteuler.net/problem=9
Question - 009
Notes: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
for num1 in range(2, 500):
    a = num1 ** 2
    for num2 in range(2, 500):
        b = num2 ** 2
        for num3 in range(2, 500):
            c = num3 ** 2
            var = a + b
            if var == c:
                # print(f"{num1} + {num2} = {num3}")
                out_value = num1 + num2 + num3
                if out_value == 1000:
                    print(f"{num1} {num2} {num3} = {out_value}")
                    break















"""
Website - projecteuler
URL - https://projecteuler.net/problem=7
Question - 007
Notes: first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import time
start_time = time.time()
count = 0
position = 10001
for each in range(2, position*100):
    # print(each)
    flag = True
    for iterate in range(2, each):
        # print(iterate)
        if each % iterate == 0:
            flag = False
            break
    if flag:
        count = count + 1
        if count == position:
            # print(f"{each} is a prime number")
            print(f"{position} prime number is {each}")
            break
end_time = time.time()
print(end_time - start_time)
    # else:
    #     print(f"{each} is a not a prime number")


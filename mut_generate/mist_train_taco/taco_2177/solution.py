"""
QUESTION:
Tod is very much focus about his English subject but now he is in trouble because he have to do his Math homework but also have to go for English classes so he asks you for help to solve his Math homework question.

You are given a  Natural number(N) you have to print Factorial of the Prime number present in the (S) series(1 ≤ S ≤ N)
INPUT

Natural number N ( 1 ≤ N ≤ 100)

OUTPUT

Factorial of all the prime number present in the series

Series contain all  element between (1 ≤ S ≤ N) 

SAMPLE INPUT
4

SAMPLE OUTPUT
2
6

Explanation

INPUT

4

OUTPUT

2 

6

In this problem series will be (1,2,3,4)

So, Prime number are(2,3)

Factorial of 2 (2*1)=2

Factorial of 3 (321)=6
"""

import math

def calculate_prime_factorials(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def factorial(num):
        prod = 1
        while num != 1:
            prod *= num
            num -= 1
        return prod

    prime_factorials = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_factorials.append(factorial(num))
    
    return prime_factorials
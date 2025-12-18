"""
QUESTION:
Design a function named `separate_numbers` that takes a list of integers as input and returns four lists containing prime numbers, composite numbers, even numbers, and odd numbers respectively. The function should be optimized to minimize the number of iterations and improve the efficiency of finding prime and composite numbers.
"""

def separate_numbers(lst):
    prime = []
    composite = []
    even = []
    odd = []

    for num in lst:
        if num < 2:
            continue
        elif num == 2:
            prime.append(num)
            even.append(num)
        elif num % 2 == 0:
            composite.append(num)
            even.append(num)
        else:
            prime_flag = True
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime.append(num)
                odd.append(num)
            else:
                composite.append(num)
                odd.append(num)

    return prime, composite, even, odd
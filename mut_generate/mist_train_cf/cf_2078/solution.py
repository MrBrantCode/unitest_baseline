"""
QUESTION:
Design a function named `separate_numbers` that takes a list of integers as input. The function should categorize the input numbers into four separate lists: prime numbers, composite numbers, even numbers, and odd numbers. The function should return these four lists. The numbers in the input list can be any integer. The function should optimize the number of iterations and improve the efficiency of finding prime and composite numbers.
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
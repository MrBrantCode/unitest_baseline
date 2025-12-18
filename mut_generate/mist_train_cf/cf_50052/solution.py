"""
QUESTION:
Implement a function `product_list(criteria, list, priority)` that calculates the product of elements in the provided list based on the specified criterion. The function should be capable of accommodating multiple criteria and implementing them accordingly. The methods should be able to apply the criteria based on the priority provided.

The function should take three parameters: 
- `criteria`: a list of criteria to be applied to the list. The criteria are represented by integers where 1 corresponds to numbers that leave a remainder of 1 when divided by 3, 2 corresponds to prime numbers, and 3 corresponds to perfect squares.
- `list`: the list of numbers to be filtered and calculated.
- `priority`: a list of integers representing the order in which the criteria should be applied.

The function should return the product of the numbers in the list that satisfy all the criteria in the given order. If no numbers satisfy all the criteria, the function should return None.
"""

from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True

def is_perfect_square(n):
    root = int(sqrt(n))
    return n == root * root

def product_list(criteria, list, priority):
    criteria_functions = {
        1: lambda x: x % 3 == 1,
        2: is_prime,
        3: is_perfect_square
    }

    filtered_list = list

    for criterion in priority:
        func = criteria_functions[criterion]
        filtered_list = [x for x in filtered_list if func(x)]

    if len(filtered_list) == 0:
        return None

    product = 1
    for x in filtered_list:
        product *= x

    return product
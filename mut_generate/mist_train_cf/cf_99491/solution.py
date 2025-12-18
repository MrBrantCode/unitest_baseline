"""
QUESTION:
Create a function `prime_composite_table` that takes a list of integers as input and returns a table with two columns, "Number" and "Prime/Composite". The "Prime/Composite" column should indicate whether the corresponding number is prime or composite. Assume the input list contains only integers. The function should be able to handle any list of integers.
"""

import math

def prime_composite_table(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    table = []
    for num in nums:
        if is_prime(num):
            table.append([num, "Prime"])
        else:
            table.append([num, "Composite"])
    return table
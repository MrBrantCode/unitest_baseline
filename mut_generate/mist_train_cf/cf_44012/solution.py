"""
QUESTION:
Write a function named `sum_divisible_by_3_and_7` that calculates the sum of unique numbers in a multi-dimensional list that are divisible by both 3 and 7. The function should be able to handle a list of any number of dimensions.
"""

from collections.abc import Iterable

def sum_divisible_by_3_and_7(lst):
    def flatten(lis):
        for item in lis:
            if isinstance(item, Iterable) and not isinstance(item, str):
                for x in flatten(item):
                    yield x
            else: 
                yield item
                
    flat_list = list(flatten(lst))
    unique_list = list(set(flat_list))
    
    divisible_by_3_and_7 = [n for n in unique_list if n % 3 == 0 and n % 7 == 0]

    return sum(divisible_by_3_and_7)
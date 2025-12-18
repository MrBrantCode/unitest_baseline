"""
QUESTION:
Write a function `sum_and_count_non_repeated` that takes a list of integers as input and returns a tuple containing the sum and count of non-repeated elements in the list. The function should work with lists containing both positive and negative integers.
"""

def sum_and_count_non_repeated(lst):
    frequency_count = {}
    for element in lst:
        if element in frequency_count:
            frequency_count[element] += 1
        else:
            frequency_count[element] = 1
    
    sum_of_non_repeated = 0
    count_of_non_repeated = 0
    
    for key, value in frequency_count.items():
        if value == 1:
            sum_of_non_repeated += key
            count_of_non_repeated += 1
    
    return sum_of_non_repeated, count_of_non_repeated
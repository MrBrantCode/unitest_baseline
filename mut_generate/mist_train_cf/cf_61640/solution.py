"""
QUESTION:
Develop a function named `discrepancy` that calculates the absolute difference between the sum of the first 'n' even integers and the sum of the first 'n' odd integers in a given list. If the list contains fewer than 'n' even or odd integers, the function should only consider the available integers. The function should be able to process negative integers and zero, and return the absolute value of the discrepancy along with the number of integers excluded from the calculation.
"""

def discrepancy(list_, n):
    even = [i for i in list_ if i % 2 == 0]
    odd = [i for i in list_ if i % 2 != 0]
    even_n = even[:n] if len(even) >= n else even
    odd_n = odd[:n] if len(odd) >= n else odd
    discrepancy = sum(even_n) - sum(odd_n)
    excluded = len(list_) - len(even_n) - len(odd_n)
    return abs(discrepancy), excluded
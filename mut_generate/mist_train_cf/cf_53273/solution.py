"""
QUESTION:
Create a function `difference_between_sums` that takes a list of integers `l` and an integer `n` as input. The function should return the difference between the sum of the first 'n' even numbers and the sum of the first 'n' odd numbers in the list. If there are less than 'n' even or odd numbers in the list, the function should sum all available numbers.
"""

def difference_between_sums(l, n):
    even = [x for x in l if x % 2 == 0]
    odd = [x for x in l if x % 2 != 0]
    return sum(even[:n]) - sum(odd[:n])
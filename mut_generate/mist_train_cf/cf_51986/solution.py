"""
QUESTION:
Write a function `count_discrepancy` that takes a list of integers `l` and a non-negative integer `n` as input. The function should calculate the absolute value of the discrepancy between the cumulative total of the first `n` even and odd integers in the list. If there are fewer than `n` even or odd integers, the function should only consider the available numbers. The function should also return the number of integers in the list that were excluded from the computation.
"""

def count_discrepancy(l, n):
    # Separate out even and odd numbers
    even_numbers = [x for x in l if x % 2 == 0]
    odd_numbers = [x for x in l if x % 2 != 0]
    
    # Calculate the sum of the first 'n' numbers
    sum_even = sum(even_numbers[:n])
    sum_odd = sum(odd_numbers[:n])

    # Calculate the number of excluded numbers
    excluded = len(l) - len(even_numbers[:n]) - len(odd_numbers[:n])
    
    # Return the absolute discrepancy and the number of excluded numbers
    return abs(sum_even - sum_odd), excluded
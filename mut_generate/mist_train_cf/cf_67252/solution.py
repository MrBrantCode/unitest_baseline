"""
QUESTION:
Write a function named `rare_value` that takes a unique, non-empty list of natural numbers as input and returns the smallest integer that is higher than zero and its frequency in the list is less than or equal to half of its value. If no such value exists, return -1.
"""

def rare_value(lst):
    # Counting the frequency of each number in the list
    freq_counter = {}
    for n in lst:
        if n in freq_counter:
            freq_counter[n] += 1
        else:
            freq_counter[n] = 1

    # Constructing a list of numbers where their frequency is less than or equal to half of their value
    rare_values = [n for n in freq_counter if freq_counter[n] <= n//2 and n > 0]

    # If there are no such numbers, returning -1
    if not rare_values:
        return -1

    # Otherwise, returning the smallest number
    return min(rare_values)
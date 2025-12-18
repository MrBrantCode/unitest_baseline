"""
QUESTION:
Write a function named `frequency_table` that takes a list of integers as input and returns a dictionary where the keys are unique integers from the list and the values are their respective frequencies. The function should be able to handle large input lists efficiently.
"""

def frequency_table(lst):
    freq_table = {}
    for num in lst:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1
    return freq_table
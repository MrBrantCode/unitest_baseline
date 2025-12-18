"""
QUESTION:
Write a function `frequency_table(lst)` that takes a list of integers `lst` and returns a dictionary where the keys are the unique integers from the list and the values are the number of times each integer appears in the list. The function should handle empty lists, negative integers, zero, and large input lists efficiently.
"""

def frequency_table(lst):
    freq_table = {}
    
    for num in lst:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1
    
    return freq_table
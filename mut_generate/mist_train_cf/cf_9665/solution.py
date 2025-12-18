"""
QUESTION:
Write a function `find_max_min_duplicates` that takes a list of integers as input. The function should return the maximum and minimum values in the list, and also print the frequency of each duplicate value. If the list is empty, print an error message and stop execution. Assume that the input list will only contain integers.
"""

def find_max_min_duplicates(lst):
    if len(lst) == 0:
        print("Error: List is empty")
        return
    
    max_value = max(lst)
    min_value = min(lst)
    
    print("Max value:", max_value)
    print("Min value:", min_value)
    
    frequencies = {}
    for num in lst:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
    
    print("Duplicate values and their frequencies:")
    for num, freq in frequencies.items():
        if freq > 1:
            print("-", num, "(", freq, "times)")
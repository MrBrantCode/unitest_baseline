"""
QUESTION:
Write a function named `most_frequent_values` that takes a list of integers as input and returns the most frequent value(s) in a list, sorted in ascending order, without using any built-in Python functions or libraries. The function should have a time complexity of O(n^2). If there are multiple values that occur with the same maximum frequency, return all of them.
"""

def most_frequent_values(lst):
    frequencies = {}
    max_freq = 0
    most_frequent_values = []
    
    for num in lst:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1
        
        if frequencies[num] > max_freq:
            max_freq = frequencies[num]
    
    for num, freq in frequencies.items():
        if freq == max_freq:
            most_frequent_values.append(num)
    
    return sorted(most_frequent_values)
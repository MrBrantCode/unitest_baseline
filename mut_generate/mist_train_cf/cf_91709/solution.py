"""
QUESTION:
Write a function `find_most_frequent(lst)` that finds the most frequent element in a list without using any built-in functions or libraries. The function should be able to handle large lists with millions of elements efficiently.
"""

def find_most_frequent(lst):
    frequency = {}
    max_count = 0
    most_frequent = None
    
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
        
        if frequency[element] > max_count:
            max_count = frequency[element]
            most_frequent = element
            
    return most_frequent
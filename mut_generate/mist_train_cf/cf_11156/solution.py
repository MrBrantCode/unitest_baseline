"""
QUESTION:
Write a function `find_most_frequent(lst)` that takes a list of elements as input and returns the most frequent element without using any built-in functions or libraries. The function should be able to handle large lists efficiently and maintain a time complexity of O(n), where n is the number of elements in the list.
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
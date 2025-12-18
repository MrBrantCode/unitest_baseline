"""
QUESTION:
Write a function named `find_duplicates` that takes an array of integers as input and returns a list of tuples, where each tuple contains a duplicate number and its frequency of occurrence. The function should consider an integer as a duplicate if it appears more than once in the array.
"""

def find_duplicates(arr):
    freq = {}
    duplicates = []
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num, count in freq.items():
        if count > 1:
            duplicates.append((num, count))
    
    return duplicates
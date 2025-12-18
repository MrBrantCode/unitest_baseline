"""
QUESTION:
Write a function `sort_elements` that takes a list of integers as input, sorts the elements based on their frequency in descending order, and returns a list of sorted elements. If multiple elements have the same frequency, they should be sorted in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_elements(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    sorted_elements = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    
    result = []
    for element in sorted_elements:
        result.append(element[0])
    
    return result
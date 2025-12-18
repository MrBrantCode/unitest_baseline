"""
QUESTION:
Create a function `remove_red_and_sort` that takes an array `arr` as input, removes all occurrences of the element "red" (case-insensitive), and returns the remaining elements sorted in alphabetical order. The function should have a time complexity not exceeding O(n^2) and a space complexity not exceeding O(n).
"""

def remove_red_and_sort(arr):
    result = []
    
    for elem in arr:
        if elem.lower() == 'red':
            continue
        result.append(elem)
    
    result.sort()
    
    return result
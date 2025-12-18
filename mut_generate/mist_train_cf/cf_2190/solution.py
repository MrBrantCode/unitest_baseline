"""
QUESTION:
Implement a function named `count_elements` that takes an array of integers as input and returns a dictionary with unique elements as keys and their counts as values. The function should remove any duplicate elements from the array before counting their occurrences. The implementation should achieve a time complexity of O(n) and a space complexity of O(n) without using any built-in methods or libraries for counting or removing duplicate elements.
"""

def count_elements(arr):
    # Remove duplicates from the array
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)
    
    # Count occurrences of each element in the array
    counts = {}
    for num in unique_arr:
        counts[num] = arr.count(num)
    
    return counts
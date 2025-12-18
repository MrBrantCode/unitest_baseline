"""
QUESTION:
Create a function called `insertion_sort_descending` that takes an array of integers as input and returns a tuple containing the number of comparisons made and the sorted array in descending order. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. The function should be able to handle edge cases such as an already sorted array, duplicate numbers, and negative numbers.
"""

def insertion_sort_descending(arr):
    comparisons = 0
    
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        # Move elements of arr[0..i-1], that are smaller than key, to one position ahead of their current position
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        
        arr[j + 1] = key
    
    return comparisons, arr
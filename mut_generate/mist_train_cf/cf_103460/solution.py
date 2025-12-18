"""
QUESTION:
Implement a function named `selection_sort` that takes a list of numbers as input and returns a new list with the numbers sorted in ascending order without using any built-in sorting functions or methods.
"""

def selection_sort(numbers):
    # Traverse through all array elements
    for i in range(len(numbers)):
        
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    
    return numbers
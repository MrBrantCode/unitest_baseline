"""
QUESTION:
Implement a function `bubble_sort_descending` that sorts a list of numbers in descending order using the Bubble Sort algorithm. The function should take a list of numbers as input and return the sorted list without using any built-in or commonly used sorting algorithms.
"""

def bubble_sort_descending(numbers):
    n = len(numbers)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1.
            # Swap if the element found is greater than the next element
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers
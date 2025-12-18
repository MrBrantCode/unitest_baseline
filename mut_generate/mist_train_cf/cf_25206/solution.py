"""
QUESTION:
Create a function named `my_sort` that takes a list of numbers as input and returns the sorted list in ascending order. Implement the sorting logic manually without using Python's built-in `sort` function or other built-in sorting methods. The input list may contain any number of unique or duplicate integers.
"""

def my_sort(numbers):
    n = len(numbers)

    for i in range(n): 
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                
    return numbers
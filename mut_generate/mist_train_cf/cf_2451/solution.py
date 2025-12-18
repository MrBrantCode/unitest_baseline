"""
QUESTION:
Implement a function called "bubble_sort" that sorts a list of integers in ascending order using the bubble sort algorithm. The input list can have a maximum length of 100 and can contain duplicate elements, with values ranging from -1000 to 1000 (inclusive). The function should take the list as an argument, return the sorted list, and include error handling to check if the input is a list of integers and if the length of the list exceeds 100, raising an exception with an appropriate error message if either condition is not met.
"""

def bubble_sort(arr):
    # Check if input is a list
    if not isinstance(arr, list):
        raise Exception("Input must be a list")
    
    # Check if input contains only integers
    if not all(isinstance(x, int) for x in arr):
        raise Exception("Input list must contain only integers")
    
    # Check if input length exceeds 100
    if len(arr) > 100:
        raise Exception("Input list length exceeds 100")
    
    # Bubble sort algorithm
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
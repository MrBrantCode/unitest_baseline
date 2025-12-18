"""
QUESTION:
Create a function called `sort_and_sum` that takes in an array of integers. Sort the array in ascending order without using any built-in sorting functions or libraries, remove any duplicate elements, and calculate the sum of the first five elements in the sorted and modified array. Return the sum of the first five elements.
"""

def sort_and_sum(arr):
    # Bubble Sort
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # Remove duplicates
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)

    # Calculate sum of the first five elements
    return sum(unique_arr[:5])
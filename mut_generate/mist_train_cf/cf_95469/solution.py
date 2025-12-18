"""
QUESTION:
Implement a function `sort_and_sum` that takes an array of integers as input. The function should sort the array in ascending order without using any built-in sorting functions or libraries. It should also remove any duplicate elements from the array. Finally, it should calculate the sum of the first five elements in the sorted and modified array and return the result. The input array may contain duplicate elements, and it may have fewer than five elements.
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
    sum_first_five = sum(unique_arr[:5])

    return sum_first_five
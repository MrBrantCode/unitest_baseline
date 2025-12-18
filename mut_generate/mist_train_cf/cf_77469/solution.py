"""
QUESTION:
Implement the function `sort_array_and_count(array)` to sort the input array in ascending order using a manual sorting algorithm (without using the built-in `sort` or `sorted` functions in Python) and return the count of numbers greater than 5 in the sorted array.
"""

def sort_array_and_count(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    
    count = 0
    for number in array:
        if number > 5:
            count += 1
    return count
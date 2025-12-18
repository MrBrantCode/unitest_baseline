"""
QUESTION:
Implement the following functions:

1. `calculate_total(arr)`: Returns the sum of all the elements in the array.
2. `calculate_average(arr)`: Returns the average of all the elements in the array.
3. `calculate_median(arr)`: Returns the median of the array by sorting the array in ascending order and handling both odd and even length cases.

Restrictions:
- The input array will always have at least one element.
- For `calculate_median(arr)`, if the length of the array is odd, return the middle element. If the length of the array is even, calculate the average of the two middle elements and return the result.
"""

def calculate_total(arr):
    return sum(arr)

def calculate_average(arr):
    return sum(arr) / len(arr)

def calculate_median(arr):
    arr.sort()
    length = len(arr)
    if length % 2 == 0:
        mid1 = arr[length // 2]
        mid2 = arr[length // 2 - 1]
        return (mid1 + mid2) / 2
    else:
        return arr[length // 2]
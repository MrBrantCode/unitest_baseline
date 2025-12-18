"""
QUESTION:
Create a Python program with two functions: `find_median(arr)` and `check_duplicates(arr)`. The `find_median(arr)` function should take an array of whole numbers as input, sort the array, and return the median without using existing statistical libraries or functions. The `check_duplicates(arr)` function should return `True` if the array contains duplicate numbers and `False` otherwise. The program should not use any existing statistical libraries or functions. The input array should be a list of integers.
"""

def entance(arr):
    def find_median(arr):
        arr.sort()
        n = len(arr)
        if n%2 == 0:
            median = (arr[n//2]+arr[n//2-1])/2
        else:
            median = arr[n//2]
        return median

    def check_duplicates(arr):
        return len(arr) != len(set(arr))

    return (find_median(arr), check_duplicates(arr))
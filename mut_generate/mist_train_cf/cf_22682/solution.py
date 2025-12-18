"""
QUESTION:
Implement a function named `print_unique_elements` that takes an array of integers as input, prints all unique elements in ascending order, and their corresponding frequencies. The function should have a time complexity of O(nlogn), where n is the size of the input array, and the array can contain negative numbers and have a size up to 10^6.
"""

def print_unique_elements(arr):
    n = len(arr)
    if n == 0:
        return

    arr.sort()

    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    arr = sorted(set(arr))
    
    for num in arr:
        print(num, frequency[num])
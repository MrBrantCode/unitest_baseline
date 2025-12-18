"""
QUESTION:
Write a function `print_unique_elements` that takes an array of integers as input, prints all the unique elements in the array in ascending order along with their frequencies, and has a time complexity of O(nlogn), where n is the size of the input array. The input array can contain negative numbers and can have a size up to 10^6.
"""

def print_unique_elements(arr):
    n = len(arr)
    if n == 0:
        return

    arr.sort()

    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    unique_arr = sorted(frequency.keys())
    for num in unique_arr:
        print(num, frequency[num])
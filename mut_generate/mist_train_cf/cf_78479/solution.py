"""
QUESTION:
Develop a function named `sort_desc_freq` that accepts a list of positive numbers as input. The function should sort the list in descending order without using the `reverse()` or `sort()` methods, and determine the frequency of each number in the list. The function should return a dictionary where the keys are the sorted numbers and the values are their corresponding frequencies.
"""

def sort_desc_freq(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    result = {}
    for i in arr:
        if i not in result:
            count = 0
            for j in arr:
                if i == j:
                    count += 1
            result[i] = count

    return result
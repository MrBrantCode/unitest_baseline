"""
QUESTION:
Implement a function `bubble_sort(arr)` that rearranges the input array in descending order using the bubble sort algorithm, ensuring all even numbers are placed before odd numbers. The solution should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def entance(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            # Compare adjacent elements and swap if in the wrong order
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # Check if the current element is odd and the next element is even, swap them
            if arr[j] % 2 != 0 and arr[j + 1] % 2 == 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
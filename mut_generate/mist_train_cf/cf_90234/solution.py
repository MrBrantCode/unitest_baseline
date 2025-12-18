"""
QUESTION:
Implement a function called `recursive_binary_search` that performs a recursive binary search in a sorted array to find the number of occurrences of a target element. The function should take a sorted array `arr` and a target element `target` as inputs and return the number of occurrences of the target element if found, or -1 if the target is not present. The function should have a time complexity of O(log n), should not use any built-in search functions or libraries, and should not use any auxiliary data structures.
"""

def recursive_binary_search(arr, target):
    def binary_search(low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            return count_occurrences(mid)
        elif arr[mid] > target:
            return binary_search(low, mid-1)
        else:
            return binary_search(mid+1, high)

    def count_occurrences(index):
        count = 1
        left = index - 1
        right = index + 1

        while left >= 0 and arr[left] == target:
            count += 1
            left -= 1

        while right < len(arr) and arr[right] == target:
            count += 1
            right += 1

        return count

    return binary_search(0, len(arr)-1)
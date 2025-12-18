"""
QUESTION:
Write a function `insert_into_sorted_array(arr, num)` that takes a sorted array of integers and an integer as input, inserts the integer into the array at the correct position while maintaining the sorted order, and returns the modified array. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the length of the array.
"""

def insert_into_sorted_array(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            arr.insert(mid, num)
            return arr

        elif arr[mid] < num:
            left = mid + 1

        else:
            right = mid - 1

    arr.insert(left, num)
    return arr
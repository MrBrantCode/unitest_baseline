"""
QUESTION:
Write a function `count_value` that counts the occurrences of a specific value in an unsorted array. The array size can be up to 10^9 and the array elements can be any integer from -10^9 to 10^9. The function should not modify the array and should have a time complexity of O(log n) or better and a space complexity of O(1).
"""

def count_value(arr, target):
    def first_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                if mid == 0 or arr[mid - 1] != target:
                    return mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def last_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                if mid == len(arr) - 1 or arr[mid + 1] != target:
                    return mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    first_occurrence_index = first_occurrence(arr, target)
    if first_occurrence_index == -1:
        return 0
    last_occurrence_index = last_occurrence(arr, target)
    return last_occurrence_index - first_occurrence_index + 1
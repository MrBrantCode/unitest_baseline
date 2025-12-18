"""
QUESTION:
Write a function named `recursive_binary_search` that takes a sorted list in descending order (`arr`), a target element (`target`), a start index (`start`), and an end index (`end`) as parameters. The function should return the index of the second occurrence of the target element in the list. If the target element appears less than twice, return -1.
"""

def recursive_binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        left_occurrence = recursive_binary_search(arr, target, start, mid - 1)
        right_occurrence = recursive_binary_search(arr, target, mid + 1, end)

        if left_occurrence == -1 and right_occurrence == -1:
            return -1
        elif left_occurrence == -1:
            return right_occurrence
        else:
            return left_occurrence
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, start, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, end)
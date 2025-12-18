"""
QUESTION:
For a given integer array `arr` and an integer `limit`, find the minimum number of elements to modify to make the array a palindrome, considering a limit on the number of unique element changes. You can change one element to any other element in a single move. If the required changes exceed the limit, return -1. Implement a function `smallest_change(arr, limit)` that returns the minimum number of elements to modify or -1 if the required changes exceed the limit.
"""

def smallest_change(arr, limit):
    def changes_required(arr, i, j, memo):
        if i >= j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if arr[i] == arr[j]:
            changes = changes_required(arr, i + 1, j - 1, memo)
        else:
            changes = 1 + min(changes_required(arr, i + 1, j, memo),
                              changes_required(arr, i, j - 1, memo))
        memo[(i, j)] = changes
        return changes
    
    memo = {}
    total_changes = changes_required(arr, 0, len(arr) - 1, memo)
    if total_changes <= limit:
        return total_changes
    else:
        return -1
"""
QUESTION:
Implement the `find_max` function that recursively finds the maximum value in an array and returns the maximum value along with the total number of comparisons made. The function takes an array of integers as input and an optional `comparisons` parameter to track the number of comparisons. If the array is empty, the function should return `None` and the total number of comparisons. The function should use a divide-and-conquer approach to find the maximum value and handle the case when there are multiple occurrences of the maximum value, returning the first occurrence.
"""

def find_max(arr, comparisons=0):
    if len(arr) == 0:
        return None, comparisons

    if len(arr) == 1:
        return arr[0], comparisons

    mid = len(arr) // 2
    left_max, comparisons = find_max(arr[:mid], comparisons)
    right_max, comparisons = find_max(arr[mid:], comparisons)

    comparisons += 1  # Increment the comparisons count only once after the recursive calls

    if left_max is None:
        return right_max, comparisons
    elif right_max is None:
        return left_max, comparisons
    elif left_max >= right_max:
        return left_max, comparisons
    else:
        return right_max, comparisons
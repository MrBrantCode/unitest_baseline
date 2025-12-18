"""
QUESTION:
Write a function `find_min_max_recursive` that finds the minimum and maximum values in a list of integers using a recursive function. The function should take in the list of integers `nums` and use indices `start` and `end` to process the list recursively. The time complexity should be O(n), where n is the number of elements in the list. Assume that the list will have at least one element.
"""

def find_min_max_recursive(nums, start, end):
    # Base case: if only one element, return it as both min and max
    if start == end:
        return (nums[start], nums[start])

    # Base case: if two elements, compare and return min and max
    if end - start == 1:
        return (min(nums[start], nums[end]), max(nums[start], nums[end]))

    # Recursive case: divide the list in two and recursively find min and max
    mid = (start + end) // 2
    left_min, left_max = find_min_max_recursive(nums, start, mid)
    right_min, right_max = find_min_max_recursive(nums, mid + 1, end)

    # Combine the results from left and right
    return (min(left_min, right_min), max(left_max, right_max))
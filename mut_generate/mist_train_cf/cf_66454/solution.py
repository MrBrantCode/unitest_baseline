"""
QUESTION:
Implement a function named `binary_search` that performs a binary search for a particular element in a pre-sorted numerical array and counts the number of occurrences of that element. The function should return the first position of the element, if it exists, in the array along with its count. The input array is guaranteed to be sorted, and the function should have a time complexity of O(log n) + O(k), where n is the size of the array and k is the number of occurrences of the element.
"""

def binary_search(array, element):
    """Implement a binary search for an element in a pre-sorted array."""
    left, right = 0, len(array) - 1
    first_pos = -1
    count = 0

    while left <= right:
        mid = left + (right - left) // 2

        # Check if element is present at the mid
        if array[mid] == element:
            first_pos = mid
            count += 1
            right = mid - 1  # Move to left part to find first position
        elif array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    if first_pos != -1:
        # Element found, let's count occurrences
        # Look to the right
        next_pos = first_pos + 1
        while next_pos < len(array) and array[next_pos] == element:
            count += 1
            next_pos += 1

    return first_pos, count
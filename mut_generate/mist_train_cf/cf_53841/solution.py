"""
QUESTION:
Implement a function `three_way_search` that performs a three-way binary search for a target element in a pre-sorted numerical array. The function should take as input the array, the left and right indices of the current search range, and the target element. The function should return the index of the target element if found, or -1 otherwise. The search should split the array into three parts in each step, with the parts being as equal in length as possible. Optimize the worst-case time complexity of the algorithm.
"""

def three_way_search(arr, l, r, target):
    if r >= l:
        mid1 = l + (r-l) // 3
        mid2 = mid1 + (r-l) // 3

        # If target is present at the mid1
        if arr[mid1] == target:
            return mid1

        # If target is present at the mid2
        if arr[mid2] == target:
            return mid2

        # If target is present in left one third
        if arr[mid1] > target:
            return three_way_search(arr, l, mid1-1, target)

        # If target is present in right one third
        if arr[mid2] < target:
            return three_way_search(arr, mid2+1, r, target)

        # If target is present in middle one third
        return three_way_search(arr, mid1+1, mid2-1, target)

    # We reach here when element is not present in array
    return -1
"""
QUESTION:
Write a function `find_largest_elements` that finds all elements in a given array which are larger than both their immediate neighbors and all their non-immediate neighbors. Implement the function using a divide and conquer approach with a time complexity requirement of O(log n).
"""

def find_largest_elements(arr):
    result = []

    def binary_search(arr, low, high):
        if low > high:
            return

        mid = low + (high - low) // 2

        # Check if the middle element is larger than both its immediate neighbors
        if (mid > 0 and arr[mid] > arr[mid-1]) and (mid < len(arr)-1 and arr[mid] > arr[mid+1]):

            # Check if the middle element is larger than all its non-immediate neighbors
            if (mid - 2 < 0 or arr[mid] > arr[mid-2]) and (mid + 2 >= len(arr) or arr[mid] > arr[mid+2]):
                result.append(arr[mid])

        # Recurse on the left half
        binary_search(arr, low, mid-1)

        # Recurse on the right half
        binary_search(arr, mid+1, high)

    # Call the binary search function on the entire array
    if len(arr) > 2:
        binary_search(arr, 1, len(arr)-2)
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            result.append(arr[0])
        else:
            result.append(arr[1])
    elif len(arr) == 1:
        result.append(arr[0])

    return result
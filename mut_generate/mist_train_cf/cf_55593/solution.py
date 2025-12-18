"""
QUESTION:
Write a function kth_element that takes three parameters: two unsorted arrays of integers and/or floating point numbers (arr1, arr2), and an integer k. The function should first sort the arrays and then find the kth smallest element in the merged array. If k is larger than the combined size of the two arrays, return an error message. The function should handle duplicate numbers and both positive and negative numbers. If the arrays contain mixed data types (e.g., integers, floating point numbers, and strings), return an error message. The time complexity of the function should be O(log(min(n,m))) where n and m are the sizes of the two arrays.
"""

def kth_element(arr1, arr2, k):
    # checking if array contains mixed data types
    if any(not isinstance(i, (int, float)) for i in arr1 + arr2):
        return 'Error: Mixed data types are not supported.'
    
    # sorting the arrays if not sorted
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    # merging the sorted arrays
    arr = arr1 + arr2
    arr.sort()

    # checking if k is out of bounds
    if k > len(arr):
        return 'Error: k is out of bounds.'
    else:
        return arr[k - 1]
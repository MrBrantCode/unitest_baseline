"""
QUESTION:
Create a function `find_common_elements` that takes two sorted arrays of integers as input and returns a new array containing the common elements between the two arrays. The function should have a time complexity of O(log n), where n is the length of the longer array, and should not use any built-in functions like `set()` or `intersection()`.
"""

def find_common_elements(arr1, arr2):
    def binary_search(arr, target):
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    common_elements = []
    for element in arr1:
        if binary_search(arr2, element):
            common_elements.append(element)
    return common_elements
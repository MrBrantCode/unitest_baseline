"""
QUESTION:
Find a function `find_common_elements(arr1, arr2)` that compares two given arrays `arr1` and `arr2`, and returns an array of their common elements in descending order, while maintaining the relative order of the elements and removing duplicates. The function should have a time complexity of O(n), where n is the length of the longer array, and a space complexity of O(m), where m is the number of unique common elements between the two arrays. The function should handle large arrays with up to 10^9 elements efficiently, and it should be case-sensitive when comparing elements.
"""

def find_common_elements(arr1, arr2):
    unique_elements = set(arr2)
    common_elements = []

    for num in arr1:
        if num in unique_elements:
            common_elements.append(num)
            unique_elements.remove(num)

    common_elements.sort(reverse=True)
    return common_elements
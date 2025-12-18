"""
QUESTION:
Create a function `find_common_elements(list1, list2)` that takes two lists as input and returns a list containing their common elements in descending order with no duplicates. The function should implement its own binary search and sorting algorithms without using built-in functions or libraries for sorting or searching.
"""

def find_common_elements(list1, list2):
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

    def remove_duplicates(arr):
        unique_elements = []
        for element in arr:
            if element not in unique_elements:
                unique_elements.append(element)
        
        return unique_elements

    def bubble_sort(arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr

    common_elements = []

    for element in list1:
        if binary_search(list2, element) and element not in common_elements:
            common_elements.append(element)

    common_elements = bubble_sort(common_elements)
    common_elements = remove_duplicates(common_elements)
    
    return common_elements
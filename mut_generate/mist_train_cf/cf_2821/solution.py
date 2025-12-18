"""
QUESTION:
Create a function called `find_common_elements` that takes two lists `list1` and `list2` as arguments. The function should return a list of elements that are present in both `list1` and `list2`, without any duplicates, and in descending order. You are not allowed to use any built-in functions or libraries for sorting or searching.
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
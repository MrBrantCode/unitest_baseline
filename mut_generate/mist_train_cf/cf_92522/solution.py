"""
QUESTION:
Write a function named `find_common_elements` that takes two unsorted arrays `arr1` and `arr2` as input and returns a list of common elements between the two arrays. The function must achieve a time complexity of O(nlogn), where n is the size of the larger array. Note that no built-in functions or data structures for sorting are allowed.
"""

def find_common_elements(arr1, arr2):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)

    def merge(left, right):
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
                j += 1
        
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged

    sorted_arr1 = merge_sort(arr1)
    sorted_arr2 = merge_sort(arr2)
    
    common_elements = []
    i = j = 0
    
    while i < len(sorted_arr1) and j < len(sorted_arr2):
        if sorted_arr1[i] < sorted_arr2[j]:
            i += 1
        elif sorted_arr1[i] > sorted_arr2[j]:
            j += 1
        else:
            common_elements.append(sorted_arr1[i])
            i += 1
            j += 1
    
    return common_elements
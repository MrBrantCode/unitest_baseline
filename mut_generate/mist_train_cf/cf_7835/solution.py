"""
QUESTION:
Implement a function `merge_and_sort` that merges two lists, `list1` and `list2`, into a single sorted list in ascending order, without using any built-in sorting functions or libraries. The function must have a time complexity of O(nlogn), where n is the total number of elements in both lists, and handle duplicates by preserving their original order. The function should also use as little extra space as possible.
"""

def merge_and_sort(list1, list2):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        left = merge_sort(left)
        right = merge_sort(right)
        
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result

    merged_list = list1 + list2
    sorted_list = merge_sort(merged_list)
    return sorted_list
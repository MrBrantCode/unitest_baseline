"""
QUESTION:
Generate a function named sort_2d_list that sorts a 2-dimensional list in ascending order based on the values of the second element in each sublist. The function should handle cases where the second element is a string or a negative number. The function should have a time complexity of O(n log n) and should not use any built-in Python sorting functions. The function should return the sorted list.
"""

def sort_2d_list(lst):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = 0
        j = 0
        
        while i < len(left) and j < len(right):
            if isinstance(left[i][1], str) and isinstance(right[j][1], str):
                if left[i][1] < right[j][1]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            elif isinstance(left[i][1], str):
                result.append(left[i])
                i += 1
            elif isinstance(right[j][1], str):
                result.append(right[j])
                j += 1
            elif left[i][1] < right[j][1]:
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
    
    return merge_sort(lst)
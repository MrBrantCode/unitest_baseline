"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts the input array in descending order without using any built-in sorting functions or methods. The input array contains integers ranging from -1000 to 1000 and its length is between 1 and 1000. The solution should have a time complexity of O(n log n), where n is the length of the input array.
"""

def merge_sort(arr):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
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

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
"""
QUESTION:
Write a function `merge_sort(lst)` that takes a list of words as input and returns the list sorted in ascending alphabetical order without using any built-in sorting functions. The function should have a time complexity of O(n log n) and handle edge cases such as empty input lists, lists filled with numbers or special characters, and non-string objects. The function should return an error message and None when the list contains non-string objects.
"""

def merge_sort(lst):
    """
    Sorts a list of words in ascending alphabetical order using the merge sort algorithm.
    
    Args:
    lst (list): A list of words to be sorted.
    
    Returns:
    list: The sorted list of words. If the list contains non-string objects, returns an error message and None.
    """
    if not all(isinstance(item, str) for item in lst):
        print("Error: List contains non-string objects")
        return None
    
    if len(lst) < 2:
        return lst

    def merge(left, right):
        if not len(left) or not len(right):
            return left or right

        result = []
        i, j = 0, 0
        while (len(result) < len(left) + len(right)):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break 

        return result

    mid = int(len(lst) / 2)
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)
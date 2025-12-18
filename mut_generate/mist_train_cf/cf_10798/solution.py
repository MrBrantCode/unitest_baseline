"""
QUESTION:
Implement a function called `print_sorted_dict_keys` that takes a dictionary as an input, prints each key-value pair in alphabetical order of the keys, and operates within O(n log n) time complexity without using any built-in sorting functions or methods.
"""

def print_sorted_dict_keys(obj):
    """
    This function takes a dictionary as an input, prints each key-value pair 
    in alphabetical order of the keys, and operates within O(n log n) time complexity.
    
    Parameters:
    obj (dict): The input dictionary.
    """
    
    # Create a list of keys
    keys = list(obj.keys())
    
    # Merge sort the keys
    def merge_sort(keys):
        if len(keys) <= 1:
            return keys
        mid = len(keys) // 2
        left_half = merge_sort(keys[:mid])
        right_half = merge_sort(keys[mid:])
        return merge(left_half, right_half)
    
    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged
    
    # Sort the keys
    sorted_keys = merge_sort(keys)
    
    # Print the key-value pairs in alphabetical order of the keys
    for key in sorted_keys:
        print(f"{key}: {obj[key]}")
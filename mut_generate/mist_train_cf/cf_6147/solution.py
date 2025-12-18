"""
QUESTION:
Write a recursive function named `add_one_recursive` that takes a list of integers as input, increments each integer by 1, and returns a new sorted list in ascending order without modifying the original list. The time complexity of the solution should be O(n log n) or better, where n is the number of elements in the list.
"""

def add_one_recursive(lst):
    """
    Recursively increments each integer in a list by 1 and returns a new sorted list in ascending order.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    list: A new sorted list with each integer incremented by 1.
    """
    
    def merge(left, right):
        """
        Merges two sorted lists into one sorted list.
        
        Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
        
        Returns:
        list: The merged sorted list.
        """
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0] + 1]
    else:
        mid = len(lst) // 2
        left = add_one_recursive(lst[:mid])
        right = add_one_recursive(lst[mid:])
        return merge(left, right)
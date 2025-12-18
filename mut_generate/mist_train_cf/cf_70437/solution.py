"""
QUESTION:
Write a function called `second_smallest_greatest` that takes a 2D list of integers with varying lengths and nested depths as input. The function should return a tuple containing the second smallest and second greatest numbers in the list. If the list contains less than two unique integers, the function should return `None`.
"""

def second_smallest_greatest(lst):
    """Find the second smallest and greatest number in a 2D list."""
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_list = flatten(lst)
    flat_list.sort()
    if len(set(flat_list)) >= 2:
        return (flat_list[1], flat_list[-2])
    else:
        return None
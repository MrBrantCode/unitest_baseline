"""
QUESTION:
Implement a function named `find_closest` that accepts a list of integers and a target value. Ensure all values in the list are negative; if not, raise an exception. Identify the value closest to the target; if multiple values are equally close, return all of them. Implement this without using Python's built-in `min` or `max` functions and utilize a sorting algorithm for optimal efficiency.
"""

def find_closest(lst, target):
    # Check if all elements in lst are negative
    for num in lst:
        if num >= 0:
            raise Exception('All elements in the list should be negative.')
    
    # Sort the list
    sorted_lst = sorted(lst, key = lambda x: abs(x - target))

    # Initialise min_diff and closest_nums
    min_diff = abs(sorted_lst[0] - target)
    closest_nums = [sorted_lst[0]]

    # Traverse the sorted list to find all closest negatives
    for i in range(1, len(sorted_lst)):
        diff = abs(sorted_lst[i] - target)
        if diff < min_diff:
            min_diff = diff
            closest_nums = [sorted_lst[i]]
        elif diff == min_diff:
            closest_nums.append(sorted_lst[i])
        else:
            break

    return closest_nums
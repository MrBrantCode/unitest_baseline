"""
QUESTION:
Write a function `assign_values` that takes two lists `list_1` and `list_2` as input. The function should assign values from `list_2` to `list_1` such that the sum of elements in `list_1` equals the sum of elements in `list_2`, and the absolute difference between adjacent elements in `list_1` is at least 2. The length of `list_1` should be half the length of `list_2`, and elements in `list_1` should be in non-decreasing order.
"""

def assign_values(list_1, list_2):
    """
    Assign values from list_2 to list_1 such that the sum of elements in list_1 equals the sum of elements in list_2,
    and the absolute difference between adjacent elements in list_1 is at least 2.
    
    Args:
    list_1 (list): The list to assign values to.
    list_2 (list): The list to assign values from.
    
    Returns:
    list: The modified list_1.
    """
    list_2.sort()  # Sort list_2 in ascending order
    half_len = len(list_2) // 2  # Calculate half the length of list_2
    list_1 = []  # Initialize an empty list for the result

    # Assign the first element of list_2 to list_1
    list_1.append(list_2[0])

    # Assign the remaining elements to list_1 with a difference of at least 2
    for i in range(1, half_len):
        # Find the next element in list_2 that is at least 2 more than the last element in list_1
        for j in range(i, len(list_2)):
            if list_2[j] - list_1[-1] >= 2:
                list_1.append(list_2[j])
                break

    return list_1
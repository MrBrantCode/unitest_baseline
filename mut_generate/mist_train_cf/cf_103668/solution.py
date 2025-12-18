"""
QUESTION:
Create a function `count_and_sort_values` that takes a list of integers as input and returns a list of dictionaries, where each dictionary contains a distinct value from the input list and its corresponding count. The output list should be sorted in descending order based on the count.
"""

def count_and_sort_values(arr):
    """
    This function takes a list of integers, counts the occurrences of each number, 
    and returns a list of dictionaries sorted in descending order based on the count.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of dictionaries containing distinct values and their counts.
    """
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    return sorted([{"Value": key, "Count": value} for key, value in count_dict.items()], key=lambda x: x["Count"], reverse=True)
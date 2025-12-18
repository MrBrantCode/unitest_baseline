"""
QUESTION:
Create a function called `sort_and_count` that takes an array of integers as input, sorts the numbers in ascending order, and maintains a count of the number of times each number appeared in the initial unsorted list. The input array may contain negative numbers and zero. The function should return two outputs: a sorted list of numbers and a dictionary where the numbers are keys and their counts are values.
"""

def sort_and_count(nums):
    """
    This function takes a list of integers, sorts them in ascending order, and counts the occurrences of each number.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    tuple: A sorted list of numbers and a dictionary where the numbers are keys and their counts are values.
    """
    
    num_dict = {}
    
    # Count the occurrences
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    # Sort the keys in ascending order
    sorted_nums = sorted(num_dict.keys())
    
    # Create the final list 
    final_list = []
    for num in sorted_nums:
        for _ in range(num_dict[num]):
            final_list.append(num)

    return final_list, num_dict
"""
QUESTION:
Write a function named `most_common_positive_integer` that finds the most common positive integer in a given list, excluding any duplicates, without using any built-in functions or data structures. The function should have a time complexity of O(n^2) or better and a space complexity of O(1).
"""

def most_common_positive_integer(numbers):
    """
    Find the most common positive integer in a list, excluding any duplicates.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        int: The most common positive integer in the list.
    """
    most_common_num = 0
    most_common_count = 0

    for i in range(len(numbers)):
        if numbers[i] == most_common_num:
            continue
        
        count = 1
        for j in range(i + 1, len(numbers)):
            if numbers[j] == numbers[i]:
                count += 1
        
        if count > most_common_count:
            most_common_count = count
            most_common_num = numbers[i]

    return most_common_num
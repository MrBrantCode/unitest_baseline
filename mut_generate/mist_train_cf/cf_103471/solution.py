"""
QUESTION:
Write a function called `most_frequent_integer_greater_than_10` that takes a list of integers as input and returns the most frequent integer greater than 10. If there are multiple integers with the same highest frequency, return any of them.
"""

def most_frequent_integer_greater_than_10(lst):
    """
    This function takes a list of integers as input and returns the most frequent integer greater than 10.
    
    If there are multiple integers with the same highest frequency, it returns any of them.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int: The most frequent integer greater than 10.
    """
    # Filter the list to include only integers greater than 10
    filtered_list = [num for num in lst if num > 10]
    
    # If the filtered list is empty, return None
    if not filtered_list:
        return None
    
    # Create a dictionary to store the frequency of each integer
    frequency_dict = {}
    for num in filtered_list:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    # Find the integer with the maximum frequency
    max_frequency = max(frequency_dict.values())
    most_frequent_num = next(num for num, freq in frequency_dict.items() if freq == max_frequency)
    
    return most_frequent_num
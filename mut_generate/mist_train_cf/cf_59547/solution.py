"""
QUESTION:
Write a function `find_highest_frequency_number` that takes a list of elements as input, determines the number exceeding 100 that recurs with the highest frequency, and returns this number. The function should handle potential errors due to different data types in the list and efficiently deal with large lists. The input list can contain integers, strings, and other non-numeric types.
"""

def find_highest_frequency_number(lst):
    """
    This function finds the number exceeding 100 that recurs with the highest frequency in a given list.
    
    Parameters:
    lst (list): A list containing integers, strings, and other non-numeric types.
    
    Returns:
    The number exceeding 100 with the highest frequency. If no such number exists, returns None.
    """
    
    number_frequency = {}
    max_frequency = 0
    max_number = None
    
    for i in lst:
        try:
            num = int(i)
            if num <= 100:
                continue
            if num in number_frequency:
                number_frequency[num] += 1
            else:
                number_frequency[num] = 1
            if number_frequency[num] > max_frequency:
                max_frequency = number_frequency[num]
                max_number = num
        except ValueError:
            continue
    
    return max_number
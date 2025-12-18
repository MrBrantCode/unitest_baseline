"""
QUESTION:
Create a function `eliminate_repetitions` that takes an array of integers as input, identifies and excludes any numbers that appear more than once in the array, and returns the resulting array containing only numbers that appear once.
"""

def eliminate_repetitions(arr):
    """
    This function eliminates any numbers that appear more than once in the given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    list: A list containing only numbers that appear once in the input array.
    """
    
    # Create a dictionary to keep track of the frequency of each number in the sequence
    dict_freq = {}
    
    # Counting frequency of each number in the sequence
    for num in arr:
        if num in dict_freq:
            dict_freq[num] += 1
        else:
            dict_freq[num] = 1
            
    # Checking if each number's frequency is 1 
    arr_clean = [num for num in arr if dict_freq[num] == 1]
    
    return arr_clean
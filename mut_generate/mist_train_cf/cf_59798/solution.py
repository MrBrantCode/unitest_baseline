"""
QUESTION:
Create a function `number_validation` that takes a string as input and returns a tuple. The string contains a combination of letters (upper and lower case), numbers, and special characters, with a length between 1 and 10^5. The function should return a boolean value indicating whether the string contains any numbers, and an integer representing the length of the longest repeating number sequence. If there are no numbers or no repeating number sequences, the integer should be 0.
"""

def number_validation(s):
    """
    This function validates a string containing a combination of letters, numbers, 
    and special characters. It returns a tuple containing a boolean indicating 
    whether the string contains any numbers and an integer representing the length 
    of the longest repeating number sequence.

    Parameters:
    s (str): The input string.

    Returns:
    tuple: A tuple containing a boolean and an integer.
    """

    # Filter the string to get only the numbers
    numbers = ''.join(filter(str.isdigit, s))
    
    # If there are no numbers, return the tuple (False, 0)
    if not numbers:
        return False, 0

    # Initialize the KMP table
    kmp_table = [0] * len(numbers)
    
    # Initialize the length of the longest prefix that is also a suffix
    length = 0
    
    # Build the KMP table
    i = 1
    while i < len(numbers):
        if numbers[i] == numbers[length]:
            length += 1
            kmp_table[i] = length
            i += 1
        elif length != 0:
            length = kmp_table[length - 1]
        else:
            kmp_table[i] = 0
            i += 1
    
    # The longest repeating sequence is the last value in the KMP table
    return True, kmp_table[-1]
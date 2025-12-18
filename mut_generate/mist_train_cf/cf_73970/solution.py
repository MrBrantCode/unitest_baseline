"""
QUESTION:
Construct a context-free grammar (CFG) to describe the language {anbmcn | n, m ≥ 0} where no two consecutive "b"s are allowed. The CFG should have production rules that start from a start symbol S and generate strings that follow the given pattern. The rules should ensure that for every 'a', there is a corresponding 'b', and 'c's can be appended any number of times or not at all. The CFG should not produce any strings with consecutive 'b's.
"""

def check_cfg(string):
    """
    Checks if a string follows the context-free grammar rules for the language {anbmcn | n, m >= 0} 
    with no two consecutive "b"s.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string follows the rules, False otherwise.
    """

    # Initialize counters for 'a's, 'b's, and 'c's
    a_count = 0
    b_count = 0
    c_count = 0

    # Initialize flag to track if we are currently processing 'c's
    processing_c = False

    # Iterate over the string
    for char in string:
        # If we encounter an 'a', increment the 'a' counter
        if char == 'a':
            a_count += 1
        # If we encounter a 'b', increment the 'b' counter
        elif char == 'b':
            b_count += 1
            # If the previous character was also a 'b', return False
            if b_count > a_count:
                return False
        # If we encounter a 'c', increment the 'c' counter and set the flag
        elif char == 'c':
            c_count += 1
            processing_c = True
        # If we encounter any other character, return False
        else:
            return False

    # If the string ended with 'c's, return True
    if processing_c:
        return True
    # If the number of 'a's is equal to the number of 'b's, return True
    elif a_count == b_count:
        return True
    # Otherwise, return False
    else:
        return False
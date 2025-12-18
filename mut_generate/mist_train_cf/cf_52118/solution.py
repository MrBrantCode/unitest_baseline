"""
QUESTION:
Create a function `total_match` that takes two lists of strings `lst1` and `lst2`, and an operation function as arguments. The operation function is a function that takes a string as input and returns a value. The function should return the list whose cumulative operation value in all the strings is equal to or less than that of the opposing list, while maintaining the chronological order of the entities within the individual lists. The function should also discard duplicate strings from both lists, retaining only the first incidence of each string, and be indifferent to text case when making string comparisons. If both lists have a similar operation value, the first list should be returned.
"""

def total_match(lst1, lst2, operation):
    '''
    Devise a function that ingests two enumerations of strings and an operation callback function, 
    outputting the enumeration whose cumulative character count in all the strings is equal to or less than 
    that of the opposing enumeration (excluding white spaces), while sustaining the chronological sequence 
    of the entities within the individual enumerations.

    Beyond this, the function is assigned the additional task of discarding duplicate strings from both 
    enumerations, while retaining only the premier incidence of each string. The function should also be 
    indifferent to text case when making string comparisons.

    If the operation argument is given, apply it to every string of the input enumerations before doing any 
    comparison. This operation could for example modify the string, count its number of vowels or compute 
    any other property to be used for the comparison.

    Should both enumerations have a similar character count according to the operation, the initial 
    enumeration is to be returned.

    The operation function argument is a function that takes a string as input and returns a value.

    :param lst1: The first list of strings
    :param lst2: The second list of strings
    :param operation: A function that takes a string as input and returns a value
    :return: The list whose cumulative operation value in all the strings is equal to or less than that 
             of the opposing list
    '''
    # Convert both lists to lower case and remove duplicates while preserving order
    lst1 = list(dict.fromkeys(map(lambda s: s.lower(), lst1)))
    lst2 = list(dict.fromkeys(map(lambda s: s.lower(), lst2)))
    
    # Apply the operation function to each string in both lists
    op1 = sum(operation(s) for s in lst1)
    op2 = sum(operation(s) for s in lst2)
    
    # Return the list with the lower or equal operation value
    return lst1 if op1 <= op2 else lst2
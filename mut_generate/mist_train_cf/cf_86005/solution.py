"""
QUESTION:
Construct a function named `filtered_list` that filters a given list containing elements of string and integer data types, where strings have more than three uppercase vowels and integers are prime numbers. The function should return the filtered list.
"""

import re

def filtered_list(lst):
    """
    Filters a given list containing elements of string and integer data types, 
    where strings have more than three uppercase vowels and integers are prime numbers.
    
    Args:
        lst (list): A list containing strings and integers.
    
    Returns:
        list: The filtered list.
    """
    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True
        else:
            return False

    def count_uppercase_vowels(word):
        return len(re.findall(r'[AEIOU]', word))

    return [x for x in lst 
            if (isinstance(x, int) and is_prime(x)) or 
            (isinstance(x, str) and count_uppercase_vowels(x) > 3)]
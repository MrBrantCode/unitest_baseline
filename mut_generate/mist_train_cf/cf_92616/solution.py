"""
QUESTION:
Create a function named `is_subsequence` that takes two strings `str1` and `str2` as parameters and returns a boolean indicating whether `str2` is a subsequence of `str1`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

def is_subsequence(str1, str2):
    # Convert the strings to lists
    lst1 = list(str1)
    lst2 = list(str2)
    
    # Initialize pointers for both lists
    i = 0  # Pointer for lst1
    j = 0  # Pointer for lst2
    
    # Traverse both lists
    while i < len(lst1) and j < len(lst2):
        # If characters match, move pointer for lst2
        if lst1[i] == lst2[j]:
            j += 1
        # Move pointer for lst1
        i += 1
    
    # If we have traversed all characters of lst2, it is a subsequence of lst1
    return j == len(lst2)
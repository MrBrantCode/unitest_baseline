"""
QUESTION:
Write a function called `check_permutation` that takes two strings as input and returns a boolean indicating whether the second string is a permutation of the first. The function should return `False` if the strings are not the same length.
"""

def check_permutation(string1, string2):
    if len(string1) != len(string2):
        # The strings can't be permutations if they are different lengths
        return False
    
    # Convert the strings to lists
    list1 = list(string1)
    list2 = list(string2)
    
    # Sort the lists to make comparison easier
    list1.sort()
    list2.sort()
    
    # Compare the elements in the sorted lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True
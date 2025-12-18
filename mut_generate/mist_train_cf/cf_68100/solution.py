"""
QUESTION:
Write a function `advanced_sequence(lst)` that takes a list of strings containing both numbers and letters as input. The function should return 'Yes' if there exists a reversed sequence of the concatenated strings that forms a palindrome, and 'No' otherwise.
"""

def advanced_sequence(lst):
    # concatenates all string items in the list in reverse to form a continuous string
    sequence = ''.join(lst[::-1])
    
    if sequence == sequence[::-1]: # checks if the string is a palindrome
        return 'Yes'
    else:
        return 'No'
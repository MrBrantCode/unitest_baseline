"""
QUESTION:
Write a function called `reverse_consonants` that takes a string as input and returns a new string where the order of consonants is reversed, while keeping vowels and special characters (including whitespace and punctuation marks) in their original positions. Do not use any built-in reverse function or extra data structures.
"""

def reverse_consonants(my_string):
    left = 0
    right = len(my_string) - 1
    vowels = "aeiouAEIOU"
    special_char = " ,.!?"
	
    my_string = list(my_string)   # Converting string to list for manipulation

    while left < right:
        if my_string[left] in vowels or my_string[left] in special_char:
            left += 1

        elif my_string[right] in vowels or my_string[right] in special_char:
            right -= 1

        else:
            my_string[left], my_string[right] = my_string[right], my_string[left]   # Swapping consonants
            left += 1
            right -= 1

    return ''.join(my_string)   # Converting list back to string
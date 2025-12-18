"""
QUESTION:
Create a function `check_anagram(string1, string2)` that determines if two input strings are anagrams of each other without using any built-in sorting functions in Python. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def check_anagram(string1, string2):
    # Check if strings are of same length
    if len(string1) != len(string2):
        return False

    # Sort the strings manually 
    sorted_string1 = sort_string(string1)
    sorted_string2 = sort_string(string2)

    # Compare the sorted strings
    for i in range(len(sorted_string1)):
        if sorted_string1[i] != sorted_string2[i]:
            return False

    return True

def sort_string(s):
    # Convert the string into list for easy sorting
    list_s = list(s)
  
    # Perform Bubble sort
    for i in range(len(list_s)):
        for j in range(i+1, len(list_s)):
            if(list_s[j] < list_s[i]):
                list_s[i], list_s[j] = list_s[j], list_s[i]

    return ''.join(list_s)
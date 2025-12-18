"""
QUESTION:
Create a function named `merge_reversed_strings` that takes two different strings as arguments, reverses the characters in each string, and merges the two reversed strings alternating characters from each. If one string runs out of characters, append the remaining characters from the other string at the end. The function should be able to handle input strings of varying lengths.
"""

def merge_reversed_strings(s1, s2):
    # Reverse both strings
    s1 = s1[::-1]
    s2 = s2[::-1]
    # Initialize an empty list to store the result
    res = []
    # Loop through each pair of characters
    for char1, char2 in zip(s1, s2):
        # Append the characters to the result list
        res.append(char1)
        res.append(char2)
    # Check for remaining characters in the longer string
    if len(s1) < len(s2):
        # Append the remaining characters from s2
        res.extend(list(s2[len(s1):]))
    else:
        # Append the remaining characters from s1
        res.extend(list(s1[len(s2):]))
    # Convert the list back into a string and return the result
    return "".join(res)
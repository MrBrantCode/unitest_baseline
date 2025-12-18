"""
QUESTION:
Write a function named `compare_strings` that takes in two strings as input and returns a list of tuples containing the index and character where the strings differ. The function should consider differences in letter casing and return the output in ascending order based on the index. The function should handle strings of different lengths.
"""

def compare_strings(string1, string2):
    differences = []
    
    # Find the minimum length between the two strings
    min_length = min(len(string1), len(string2))
    
    # Iterate over the characters of the strings and compare them
    for i in range(min_length):
        if string1[i] != string2[i]:
            differences.append((i, string1[i]))
            differences.append((i, string2[i]))
    
    # Check if there are additional characters in string2
    if len(string1) < len(string2):
        for i in range(min_length, len(string2)):
            differences.append((i, string2[i]))
    
    # Check if there are additional characters in string1
    elif len(string1) > len(string2):
        for i in range(min_length, len(string1)):
            differences.append((i, string1[i]))
    
    # Sort the differences list based on the index
    differences.sort(key=lambda x: x[0])
    
    return differences
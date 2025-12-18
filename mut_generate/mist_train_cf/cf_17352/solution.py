"""
QUESTION:
Create a function named `count_occurrences` that takes a string as input and returns a dictionary where the keys are the characters in the string and the values are the number of occurrences of each character. The input string should contain only lowercase alphabets and have a length between 1 and 1000 characters. The function must be implemented without using any built-in Python functions or libraries for counting occurrences or creating dictionaries.
"""

def count_occurrences(string):
    occurrences = {}
    
    for char in string:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    
    return occurrences
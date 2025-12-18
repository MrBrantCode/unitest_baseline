"""
QUESTION:
Create a function called `replace_and_count` that takes a string as input and replaces all instances of the letter "e" with "X". The function should also count the number of occurrences of the letter "e" in the string. The function should run in O(n) time complexity and use O(n) additional space, where n is the length of the input string. The input string will have a maximum length of 10^6 characters.
"""

def replace_and_count(string):
    count = 0
    replaced_string = ""
    
    for char in string:
        if char == "e":
            count += 1
            replaced_string += "X"
        else:
            replaced_string += char
    
    return replaced_string, count
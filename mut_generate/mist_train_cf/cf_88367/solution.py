"""
QUESTION:
Write a Python function called "capitalize_array" that takes in a nested list "A" as a parameter, where each element of the nested list is a string. The function should capitalize the first letter of each word in each string element of the nested list and return the modified nested list. You are not allowed to use any built-in Python functions or methods for capitalizing strings.
"""

def capitalize_array(A):
    def capitalize_string(s):
        capitalized_string = ""
        for word in s.split():
            capitalized_string += word[0].upper() + word[1:] + " "
        return capitalized_string.strip()

    capitalized_array = []
    for sublist in A:
        capitalized_sublist = []
        for string in sublist:
            capitalized_sublist.append(capitalize_string(string))
        capitalized_array.append(capitalized_sublist)
    return capitalized_array
"""
QUESTION:
Create a function called `merge_strings` that accepts two string inputs. The function should return a new string containing the first three characters of each input string, but only if these characters are alphabets. If the input string has less than three characters or the first three characters are not alphabets, they should be ignored. The function should also support Unicode inputs.
"""

def merge_strings(string1, string2):
    result = ""
    
    # Check if the initial 3 characters in each string are alphabets
    for s in (string1, string2):
        if len(s) >= 3 and s[:3].isalpha():
            result += s[:3]

    return result
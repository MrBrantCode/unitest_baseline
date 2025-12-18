"""
QUESTION:
Create a function named `find_strings_with_substring` that takes in a list of strings (`lst`) and a target string (`target`). The function should print each string in the list that contains the target string as a substring, ignoring case sensitivity, and return the count of such strings.
"""

def find_strings_with_substring(lst, target):
    count = 0
    for string in lst:
        if target.lower() in string.lower():
            print(string)
            count += 1
    return count
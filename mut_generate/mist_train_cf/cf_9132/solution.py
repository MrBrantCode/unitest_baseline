"""
QUESTION:
Create a function called `convert_and_append` that takes a list of strings as input, converts all the strings to uppercase, and then appends the string "Welcome to the party" at the end of the list. The function should return the modified list.
"""

def convert_and_append(lst):
    for i in range(len(lst)):
        lst[i] = lst[i].upper()
    lst.append("Welcome to the party")
    return lst
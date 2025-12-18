"""
QUESTION:
Implement the function `announce_all` that takes a list of names as input and returns a string announcing each name in the list. The function should capitalize the first letter of each name, separate each name by a comma and a space, except for the last name which should be preceded by "and" instead. If the input list is empty, return an empty string.
"""

def announce_all(names):
    if not names:
        return ""
    elif len(names) == 1:
        return names[0].capitalize()
    else:
        announced_names = [name.capitalize() for name in names[:-1]]
        announced_names.append("and " + names[-1].capitalize())
        return ", ".join(announced_names)
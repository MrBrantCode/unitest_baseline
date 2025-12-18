"""
QUESTION:
Create a function named `compose_strings` that takes two lists of strings as input, one for names and one for blank phrases. The function should return a new list of strings where each name is combined with each blank phrase. The names and blank phrases should be joined by replacing the double underscore ("__") in the blank phrase with the name. 

The function should have no additional parameters other than the two input lists, and it should return the composed list of strings.
"""

def compose_strings(names, blanks):
    return [blank.replace("__", name) for name in names for blank in blanks]
"""
QUESTION:
Write function describeList which returns "empty" if the list is empty or "singleton" if it contains only one element or "longer"" if more.
"""

def describe_list(lst):
    if len(lst) == 0:
        return "empty"
    elif len(lst) == 1:
        return "singleton"
    else:
        return "longer"
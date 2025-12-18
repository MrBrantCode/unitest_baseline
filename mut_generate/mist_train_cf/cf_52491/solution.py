"""
QUESTION:
Create a function named `create_dict_list` that takes an integer `N` as input and returns a list of `N` dictionaries. Each dictionary should have a unique identifier as a key in the format 'idX' where X is the dictionary's index, and the value associated with this key should be an empty dictionary.
"""

def create_dict_list(N):
    return [{'id'+str(i):{}} for i in range(N)]
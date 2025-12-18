"""
QUESTION:
Write a Python function `find_key_in_tuple` that takes a tuple and a variable `k` as input and returns `True` if `k` is found in the tuple or any nested tuple, and `False` otherwise.
"""

def find_key_in_tuple(tuple_input, k):
    def search_in_tuple(t):
        if not isinstance(t, tuple):
            return False
        if k in t:
            return True
        for item in t:
            if search_in_tuple(item):
                return True
        return False

    return search_in_tuple(tuple_input)
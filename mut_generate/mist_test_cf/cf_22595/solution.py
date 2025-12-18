"""
QUESTION:
Implement a function `is_unique_list` that checks if all items in a list are unique, handling the case where the list contains nested lists and/or dictionaries, without using any built-in functions or data structures for checking uniqueness.
"""

def is_unique_list(lst):
    seen = []
    def is_unique(lst):
        for i in lst:
            if isinstance(i, list):
                if not is_unique(i):
                    return False
            elif isinstance(i, dict):
                keys = list(i.keys())
                for key in keys:
                    if i[key] in seen:
                        return False
                    seen.append(i[key])
                    if isinstance(i[key], (list, dict)):
                        if not is_unique([i[key]]):
                            return False
            else:
                if i in seen:
                    return False
                seen.append(i)
        return True
    return is_unique(lst)
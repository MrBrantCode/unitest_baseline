"""
QUESTION:
Create a function named `unique_string_arrangement` that takes a tuple `t` consisting of string data types, and returns a tuple with distinct elements in alphabetical order. The function must not use Python's built-in `sort` function or `set` data structure.
"""

def unique_string_arrangement(t: tuple):
    """Return alphabetically arranged unique elements in a tuple without using inbuilt sort function or set"""
    t = list(t)

    # Bubble sort
    for i in range(len(t)):
        for j in range(len(t) - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]

    # Remove duplicates
    i = 1
    while i < len(t):
        if t[i] == t[i - 1]:
            del t[i]
        else:
            i += 1

    return tuple(t)
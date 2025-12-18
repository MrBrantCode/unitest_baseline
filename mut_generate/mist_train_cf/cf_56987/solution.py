"""
QUESTION:
Implement a function named `Boyer_Moore_search` that takes two parameters: `text` and `pattern`. The function should perform a case-insensitive search for the last occurrence of `pattern` in `text` without using Python's built-in string search function. The function should return the starting index of the last occurrence of the `pattern` in the `text`. If the `pattern` is not found, the function should return -1.
"""

def Boyer_Moore_search(text, pattern):
    """
    Perform a case-insensitive search for the last occurrence of `pattern` in `text` without using Python's built-in string search function.
    
    Parameters:
    text (str): The text to search in.
    pattern (str): The pattern to search for.
    
    Returns:
    int: The starting index of the last occurrence of the `pattern` in the `text`. If the `pattern` is not found, returns -1.
    """
    text = text.lower()
    pattern = pattern.lower()

    n, m = len(text), len(pattern)
    if m == 0: 
        return 0
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m-1
    k = m-1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1
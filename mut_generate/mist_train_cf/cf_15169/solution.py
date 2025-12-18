"""
QUESTION:
Implement a function called `pattern_search` that takes in two parameters: a string called `text` and a string called `pattern`. The function should return the number of occurrences of the `pattern` in the `text` using a nested for loop. The outer loop should iterate over each character in the text, while the inner loop should iterate over each character in the pattern. The function should be optimized to minimize time complexity.
"""

def pattern_search(text, pattern):
    """
    Searches for occurrences of a pattern in a given text using a nested loop.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        int: The number of occurrences of the pattern in the text.
    """
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            count += 1
    return count
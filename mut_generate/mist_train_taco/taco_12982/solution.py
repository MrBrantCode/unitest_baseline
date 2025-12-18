"""
QUESTION:
Complete the function that takes one argument, a list of words, and returns the length of the longest word in the list.

For example: 

```python
['simple', 'is', 'better', 'than', 'complex'] ==> 7
```

Do not modify the input list.
"""

def find_longest_word_length(words):
    """
    Returns the length of the longest word in the given list of words.

    Parameters:
    words (list of str): A list of words.

    Returns:
    int: The length of the longest word in the list.
    """
    return max(map(len, words))
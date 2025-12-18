"""
QUESTION:
Implement the `helper` method in the `Solution` class, which takes a string `s` and a set of words `wordDict` as parameters, and returns a boolean value indicating whether the string `s` can be segmented into a space-separated sequence of one or more dictionary words using a recursive approach. The `Solution` class is initialized with the `wordDict`.
"""

def word_break(s, wordDict):
    """
    Returns a boolean value indicating whether the string `s` can be segmented into a space-separated sequence of one or more dictionary words.
    
    :param s: The input string to be segmented.
    :param wordDict: A set of words.
    :return: True if the string `s` can be segmented into words from `wordDict`, False otherwise.
    """
    if not s:
        return True  # Base case: empty string can be segmented
    for i in range(1, len(s) + 1):
        if s[:i] in wordDict and word_break(s[i:], wordDict):
            return True
    return False
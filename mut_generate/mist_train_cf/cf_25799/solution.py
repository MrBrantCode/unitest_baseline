"""
QUESTION:
Write a function `kth_most_frequent` that takes a string `s` and an integer `k` as input and returns the kth most frequent word in the string. The string is separated by spaces and the comparison is case sensitive. If there are multiple words with the same frequency, the one that appears first in the sorted list of words is considered more frequent. The function should return the word as a string. The input string `s` only contains letters and spaces.
"""

def kth_most_frequent(s, k):
    """
    Returns the kth most frequent word in a given string.
    
    Parameters:
    s (str): The input string.
    k (int): The position of the word in the frequency list.
    
    Returns:
    str: The kth most frequent word.
    """
    counts = {}
    words = s.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    return sorted(counts, key=counts.get, reverse=True)[k-1]
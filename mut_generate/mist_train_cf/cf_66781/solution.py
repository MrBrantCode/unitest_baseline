"""
QUESTION:
Construct a function named `freq_counter` that takes a nested list `nested_lst` and a word `word` as parameters. The function should return the frequency of the word within the nested list, considering both complete and partial matches. The function should handle a mix of strings and integers in the nested list. The function should be recursive to handle nested lists of arbitrary depth.
"""

def freq_counter(nested_lst, word):
    freq = 0
    for n in nested_lst:
        if isinstance(n, list):
            freq += freq_counter(n, word)
        elif isinstance(n, str) and word in n:
            freq += 1
    return freq
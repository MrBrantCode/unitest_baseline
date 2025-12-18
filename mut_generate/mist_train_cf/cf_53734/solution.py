"""
QUESTION:
Write a function named `solve` that takes a list of strings `lst` and a dictionary of strings `dict` as input. The function should return a list of tuples, where each tuple contains a string from `lst` with a length greater than 4 and not a key in `dict`, along with a dictionary containing the frequency of vowels in that string. The function should consider both lowercase and uppercase vowels, and its time complexity should not exceed O(n^2), where n is the total number of characters across all strings in `lst`.
"""

def solve(lst, dict):
    vowels = 'aeiouAEIOU'
    output = []
    for word in lst:
        if len(word) > 4 and word not in dict:
            vowel_dict = {v: word.count(v) for v in vowels if word.count(v) > 0}
            output.append((word, vowel_dict))
    return output
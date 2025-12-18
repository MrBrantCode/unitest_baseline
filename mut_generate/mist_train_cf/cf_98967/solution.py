"""
QUESTION:
Write a Python function named `is_anagram_array` that takes a list of strings as input and returns a boolean indicating whether every string in the array is an anagram of every other string. The function should handle arrays containing duplicate strings and have a time and space-efficient algorithm.
"""

def is_anagram_array(arr: list[str]) -> bool:
    n = len(arr)
    
    # create a dictionary to store frequency of characters in each string
    freq_dict = {}
    for i in range(n):
        s = arr[i]
        freq_dict[i] = {}
        for c in s:
            freq_dict[i][c] = freq_dict[i].get(c, 0) + 1
    
    # compare the frequency dictionary of each string to check if they are anagrams
    for i in range(n):
        for j in range(i+1, n):
            if freq_dict[i] != freq_dict[j]:
                return False
    
    return True
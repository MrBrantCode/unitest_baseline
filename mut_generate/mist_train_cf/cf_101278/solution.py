"""
QUESTION:
Write a function `is_anagram_array(arr)` that determines whether every string in an array `arr` is an anagram of every other string in the array. The function should handle arrays containing duplicate strings and have a time and space-efficient algorithm to handle arrays of any length and complexity.
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
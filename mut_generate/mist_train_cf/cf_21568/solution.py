"""
QUESTION:
Given the function name `kth_largest_character(s, k)`, write a function that finds the kth largest character in a string `s` based on the frequency of each character. Here, `s` is a string of ASCII characters with a maximum length of 10^6 and `k` is an integer between 1 and the number of unique characters in `s`. The function should return the character with the kth highest frequency.
"""

def kth_largest_character(s, k):
    # Initialize a dictionary to count the frequency of each character in s
    freq = {}
    
    # Count the frequency of each character
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    # Sort the unique characters in s based on their frequencies in descending order
    sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
    
    # Return the kth largest character
    return sorted_chars[k-1]
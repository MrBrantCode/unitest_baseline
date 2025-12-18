"""
QUESTION:
Given a string s and an integer k, write a function named kth_largest_character that returns the kth largest character of s. The characters in s are ASCII characters, the length of s is at most 10^5, and 1 <= k <= the number of unique characters in s. The kth largest character is determined by the frequency of each character in descending order.
"""

def entance(s, k):
    # Initialize a dictionary to keep track of the frequency of each character in the string.
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # Convert the dictionary into a list of tuples, where each tuple contains a character and its frequency.
    freq_list = [(char, freq) for char, freq in freq_dict.items()]

    # Sort the list of tuples in descending order based on the frequency.
    freq_list.sort(key=lambda x: x[1], reverse=True)

    # Return the kth character from the sorted list.
    return freq_list[k-1][0]
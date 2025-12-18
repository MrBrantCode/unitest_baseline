"""
QUESTION:
Generate a Frequency Table for a given sequence of characters using a dictionary data structure and implement a function to calculate the top k most frequent characters in the sequence. The input sequence can contain any printable ASCII characters and can have a length of up to 10^6 characters.

Create two functions: `generate_frequency_table(sequence)` and `top_k_frequent_chars(sequence, k)`. The `generate_frequency_table(sequence)` function should have a time complexity of O(n), where n is the length of the input sequence. The `top_k_frequent_chars(sequence, k)` function should take the input sequence and the value of k as parameters, return a list of the top k most frequent characters in descending order of frequency, and have a time complexity of O(n log k). If two characters have the same frequency, the character with the lower ASCII value should come first.
"""

def generate_frequency_table(sequence):
    freq_table = {}
    for char in sequence:
        freq_table[char] = freq_table.get(char, 0) + 1
    return freq_table

def top_k_frequent_chars(sequence, k):
    freq_table = generate_frequency_table(sequence)
    top_k_chars = sorted(freq_table.keys(), key=lambda x: (-freq_table[x], ord(x)))
    return top_k_chars[:k]
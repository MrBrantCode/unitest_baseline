"""
QUESTION:
Write a function `k_most_frequent_words` that takes in a list of strings `words` and an integer `k`, and returns a list of the k most frequent words in lexicographical order. The function should be case-sensitive and consider words with the same frequency in lexicographical order. 

The input list of strings is not empty, and the value of k is greater than or equal to 1 and less than or equal to the number of unique words in the input list. The input list of strings contains only alphabets, the length of each word is between 1 and 100, and the total number of words is between 1 and 10^4.
"""

def k_most_frequent_words(words, k):
    # Count the frequency of each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort the dictionary by frequency and then by lexicographical order
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    # Extract the k most frequent words
    k_most_frequent = [word[0] for word in sorted_words[:k]]

    return k_most_frequent
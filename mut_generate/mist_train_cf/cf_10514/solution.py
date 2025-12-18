"""
QUESTION:
Given a list of n strings and an integer k, write a function `find_k_most_frequent_words` that returns the k most frequent words in the list. If multiple words have the same frequency, return them in lexicographical order. The function should take two parameters: a list of strings `words` and an integer `k`. The function should return a list of strings.
"""

def find_k_most_frequent_words(words, k):
    # Create a dictionary to store the count of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the words based on their count and lexicographical order
    sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))
    
    # Return the first k words from the sorted list
    return sorted_words[:k]
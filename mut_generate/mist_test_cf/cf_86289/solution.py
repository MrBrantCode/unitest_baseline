"""
QUESTION:
Write a function `get_top_10_words(string)` that takes a string as input and returns the top 10 most common words in the string, excluding common stop words such as "the", "and", "a", "is", etc. The function should run in O(nlogn) time complexity, where n is the length of the input string.
"""

import heapq
import re

def get_top_10_words(string):
    stopwords = {"the", "and", "a", "is"}  
    word_freq = {}  

    for word in re.findall(r'\w+', string.lower()):
        if word not in stopwords:
            word_freq[word] = word_freq.get(word, 0) + 1

    heap = []  

    for word, freq in word_freq.items():
        if len(heap) < 10:
            heapq.heappush(heap, (freq, word))
        else:
            if freq > heap[0][0]:
                heapq.heappushpop(heap, (freq, word))

    top_10_words = [pair[1] for pair in heapq.nlargest(10, heap)]

    return top_10_words
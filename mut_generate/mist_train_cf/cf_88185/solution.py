"""
QUESTION:
Develop a function `top_k_common_words` that takes two parameters: `text` (a string that may contain special characters and punctuation marks) and `k` (an integer representing the number of top common words to return). The function should return the top K most commonly used words in the given text, ignoring special characters and punctuation marks, and handling large input texts efficiently with a time complexity of O(nlogk), where n is the number of words in the text.
"""

import re
import heapq

def top_k_common_words(text, k):
    words = re.findall(r'\w+', text.lower())
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    heap = []
    for word, freq in word_freq.items():
        heapq.heappush(heap, (freq, word))
        if len(heap) > k:
            heapq.heappop(heap)

    top_k_words = []
    while heap:
        top_k_words.append(heapq.heappop(heap)[1])

    return top_k_words[::-1]
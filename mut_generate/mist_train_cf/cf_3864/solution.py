"""
QUESTION:
Develop a function named `top_k_common_words` that takes a string `text` and an integer `k` as input parameters. The function should return the top K most commonly used words in the given text, ignoring special characters and punctuation marks. The time complexity of the function should be O(nlogk), where n is the number of words in the text. The returned list of words should be in descending order of frequency.
"""

import re
import heapq

def top_k_common_words(text, k):
    # Step 1: Split the text into words
    words = re.findall(r'\w+', text.lower())

    # Step 2: Count the frequency of each word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Step 3: Build a min-heap
    heap = []
    for word, freq in word_freq.items():
        heapq.heappush(heap, (freq, word))

        # Step 4: Limit the heap size to K
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 5: Extract the top K most common words
    top_k_words = []
    while heap:
        top_k_words.append(heapq.heappop(heap)[1])

    return top_k_words[::-1]  # Reverse the list to get descending order of frequency
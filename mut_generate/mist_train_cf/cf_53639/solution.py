"""
QUESTION:
Develop a function `sentence_to_priority_queue(sentence)` that takes a string sentence as input, isolates individual words, and returns a list of words in a priority order sorted by word length in descending order. If multiple words have the same length, maintain their original order of appearance. The function should ignore any punctuation and be case insensitive.
"""

import re
import heapq 

def sentence_to_priority_queue(sentence):
    # remove punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)
    
    # convert to lowercase
    sentence = sentence.lower()

    # split words
    words = sentence.split()

    # define a comparator for the priority queue
    class Word:
        def __init__(self, word):
            self.word = word
            self.length = len(word)

        def __lt__(self, other):
            return self.length > other.length
    
    # push words into the priority queue
    # since heapq is a min-heap, we use negative length as key to simulate a max-heap
    priority_queue = []
    for word in words:
        heapq.heappush(priority_queue, Word(word))

    # pop and return words in the reverse order
    return [heapq.heappop(priority_queue).word for _ in range(len(priority_queue))]
"""
QUESTION:
Implement a function named `word_counter` that takes two strings `sentence1` and `sentence2` as input, and returns the count of unique words that appear in both sentences along with their respective counts. The function should be case-insensitive and ignore special characters. 

Restrictions: 
- The function should handle special characters by replacing them with a space.
- It should ignore case sensitivity by converting both sentences to lower case.
- It should count the unique words that appear in both sentences, not just the unique words overall.
- The function should output the count of unique words in both sentences and the unique words along with their counts.
"""

import re

def word_counter(sentence1, sentence2):
    # Converting to lower case and removing special characters
    sentence1, sentence2 = re.sub(r'\W+', ' ', sentence1.lower()), re.sub(r'\W+', ' ', sentence2.lower())
    
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    common_words = set1.intersection(set2)
    
    word_count = {}
    
    # Counting each word in both the sentences
    for word in common_words:
        count1 = sentence1.split().count(word)
        count2 = sentence2.split().count(word)
        word_count[word] = (count1, count2)

    return len(common_words), word_count
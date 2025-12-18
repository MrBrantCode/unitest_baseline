"""
QUESTION:
Develop a function `solve(seq)` that takes a string `seq` as input, where `seq` is a character sequence separated by hyphens. The function should split `seq` into words using the hyphen as a delimiter, count the frequency of each word, and then sort and display the resultant words in the order of their increasing frequency. If multiple words have the same frequency, they should be sorted alphabetically while preserving their case (i.e., treating uppercase and lowercase words as different). The output should be a list of word-frequency pairs.
"""

def solve(seq):
    words_frequency = {}
    words  = seq.split('-')
    for word in words:
        words_frequency[word] = words_frequency.get(word,0) + 1
    
    sorted_words = sorted(words_frequency.items(), key=lambda x: (x[1], x[0]))
    
    return sorted_words
"""
QUESTION:
Given a string of distinct alphabetical symbols and a list of words (linguistic lexicon), implement a function named `find_longest_word` that returns the longest word from the lexicon that can be formed using the given alphabetical symbols. The function must respect frequency constraints, i.e., the frequency of each letter in the word should not exceed its frequency in the given alphabetical symbols. The comparison should be case-insensitive.
"""

def find_longest_word(cluster, lexicon):
    cluster = cluster.lower()  
    max_length = 0
    longest_word = ""

    for word in lexicon:
        word = word.lower()  
        word_valid = True
        for letter in word:
            if word.count(letter) > cluster.count(letter):
                word_valid = False
                break
        if word_valid and len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word
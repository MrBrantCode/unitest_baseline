"""
QUESTION:
Write a function named `common_words` that takes two input parameters, `sentence1` and `sentence2`, and returns the count of distinct words common to both sentences, ignoring case and punctuation. The function should consider only word-level matching, treating punctuation as part of the word.
"""

def common_words(sentence1, sentence2):
    # Tokenizing the sentences into words and converting to set for easy comparison
    words_in_sentence1 = set(sentence1.lower().split())
    words_in_sentence2 = set(sentence2.lower().split())
  
    # Intersecting the sets to get common words
    common_words = words_in_sentence1 & words_in_sentence2
  
    # Count of distinct common words
    return len(common_words)
"""
QUESTION:
Write a function `check_jaccard_similarity(sentence1, sentence2)` that calculates the Jaccard similarity coefficient between two input sentences. The function should ignore case and punctuation. Implement the code to handle large sentences efficiently without using any built-in or external libraries for set operations.
"""

def check_jaccard_similarity(sentence1, sentence2):
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    ignore = ['!', '"', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', ':', ';', '<', '>', '=', 
             '?', '@', '[', ']', '^', '_', '`', '{', '}', '|', '~'] # List of punctuation marks
    
    sentence1_words = "".join((char for char in sentence1 if char not in ignore)).split()
    sentence2_words = "".join((char for char in sentence2 if char not in ignore)).split()

    common_words = 0

    sentence1_map = {}
    for word in sentence1_words:
        if word not in sentence1_map:
            sentence1_map[word] = True
            if word in sentence2_words:
                common_words += 1

    total_distinct_words = len(sentence1_map) + len([word for word in sentence2_words if word not in sentence1_map])
  
    jaccard_similarity = common_words / total_distinct_words
    
    return jaccard_similarity
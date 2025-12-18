"""
QUESTION:
Write a function named `remove_duplicates` that takes a sentence as input and returns a modified sentence where any duplicate words are removed except for their first occurrence. The words in the modified sentence should maintain their original order.
"""

def remove_duplicates(sentence):
    words = sentence.split()
    seen_words = set()
    result = []
    
    for word in words:
        if word not in seen_words:
            result.append(word)
            seen_words.add(word)
    
    return ' '.join(result)
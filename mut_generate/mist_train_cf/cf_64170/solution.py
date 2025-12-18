"""
QUESTION:
Create a function called `reverse_order` that takes a 2D array of characters as input, where each sub-array represents words in a sentence. The function should reverse the order of words within each sentence and then reverse the order of the sentences themselves. The solution should have optimized time complexity.
"""

def reverse_order(sentences):
    # Reverse order of words in each sentence
    for i in range(len(sentences)):
        sentences[i] = sentences[i][::-1]
    
    # Reverse order of sentences
    sentences = sentences[::-1]
    
    return sentences
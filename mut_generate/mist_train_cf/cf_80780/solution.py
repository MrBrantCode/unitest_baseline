"""
QUESTION:
Given two sentences `A` and `B`, each consisting of lowercase alphabets and spaces with a maximum length of 200 characters, implement a function `uncommonFromSentences` that returns a list of uncommon words. An uncommon word is a word that appears in one sentence but not the other. The order of the words in the list does not matter.
"""

def uncommonFromSentences(A, B):
    """
    Returns a list of uncommon words from two given sentences.
    
    Args:
    A (str): The first sentence.
    B (str): The second sentence.
    
    Returns:
    list: A list of uncommon words.
    """
    words = (A + " " + B).split()
    count = {}
    
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    return [word for word, freq in count.items() if freq == 1]
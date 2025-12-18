"""
QUESTION:
Write a function named `extract_A_words` that takes a list of sentences as input and returns a list of unique words that start with the letter 'a' or 'A'. The function should be case-insensitive and should not include any duplicate words in the output.
"""

def extract_A_words(sentences):
    A_words = set()  
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word[0].lower() == 'a':  
                A_words.add(word)
    return list(A_words)
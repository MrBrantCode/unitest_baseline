"""
QUESTION:
Write a function named `check_duplicate` to filter sentences from a list of sentences. The function should exclude sentences containing more than 10 words or duplicate words. The function should account for case sensitivity. The input is a list of strings where each string represents a sentence. The output should be a list of filtered sentences.
"""

def check_duplicate(sentences):
    filtered_sentences = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) <= 10 and len(words) == len(set(words)):
            filtered_sentences.append(sentence)
    return filtered_sentences
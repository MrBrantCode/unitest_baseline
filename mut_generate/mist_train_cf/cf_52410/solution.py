"""
QUESTION:
Write a function `convert_to_title_case(s)` that converts a given string `s` to title case, handling special characters and numbers within the string, and capitalizing the first letter of each sentence. The function should split sentences by ". " (a period followed by a space), and consider a sentence as a sequence of characters between two ". " delimiters.
"""

def convert_to_title_case(s):
    sentences = s.split('. ')
    title_case_sentences = [sentence.title() for sentence in sentences]
    return '. '.join(title_case_sentences)
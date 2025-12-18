"""
QUESTION:
Write a function named `get_python_sentences` that takes a string of text as input and returns a string containing only the sentences with the word 'Python'. The sentences are separated by full stops. The function should be case-sensitive and consider 'Python' and 'python' as different words.
"""

def get_python_sentences(text):
    sentences = text.split('.')
    python_sentences = [sentence.strip() + '.' for sentence in sentences if 'Python' in sentence]
    return ' '.join(python_sentences)
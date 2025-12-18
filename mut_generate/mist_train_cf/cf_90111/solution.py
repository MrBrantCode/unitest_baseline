"""
QUESTION:
Implement a function named `generate_paragraph` that takes a string `input_text` as input. The function should split the input text into individual sentences by using punctuation marks as delimiters, remove any repeated sentences, and concatenate the remaining sentences together to form a paragraph. Ensure that each sentence in the generated paragraph ends with a punctuation mark.
"""

import re

def generate_paragraph(input_text):
    # Split the input text into individual sentences by using punctuation marks as delimiters
    sentences = re.split('([.!?])', input_text)
    
    # Remove any repeated sentences from the list of generated sentences
    unique_sentences = []
    for i in range(0, len(sentences), 2):
        sentence = sentences[i] + sentences[i+1] if i+1 < len(sentences) else sentences[i]
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)
            
    # Concatenate the sentences together to form a paragraph
    paragraph = ''.join(unique_sentences)
    return paragraph
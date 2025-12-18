"""
QUESTION:
Write a function `generate_summary(text, max_words)` that takes a string of English text and an integer `max_words` as input, and returns a summary of the text limited to `max_words` words. The summary should capture the main ideas and key details of the original text. The input text may be large, and the function should handle it efficiently without performance issues.
"""

import re
import heapq
from collections import Counter

def generate_summary(text, max_words):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    tokens = re.findall(r'\b\w+\b', text.lower())
    stopwords = set(['the', 'and', 'in', 'etc.'])  
    tokens = [token for token in tokens if token not in stopwords]
    word_frequency = Counter(tokens)
    sentence_scores = []
    for sentence in sentences:
        sentence_tokens = [token for token in re.findall(r'\b\w+\b', sentence.lower()) if token not in stopwords]
        sentence_score = sum(word_frequency[token] for token in sentence_tokens)
        sentence_scores.append((sentence_score, sentence))
    top_sentences = heapq.nlargest(max_words, sentence_scores, key=lambda x: x[0])
    summary = ' '.join(sentence for _, sentence in top_sentences)
    return summary
"""
QUESTION:
Write a function named "summarize_article" that takes a text as input and returns a one-sentence summary of the article. The input text will be a short paragraph describing a topic. The function should return a string that summarizes the main idea of the topic.
"""

def summarize_article(text):
    sentences = text.split('. ')
    summary_sentence = max(sentences, key=len)
    return summary_sentence
"""
QUESTION:
Create a function `sentiment_analysis(text: str, positive_words: List[str], negative_words: List[str]) -> str` that determines the sentiment of a given text by comparing the count of positive and negative words. The function should take in three parameters: the input text, a list of positive words, and a list of negative words. It should return "Positive" if the count of positive words is greater, "Negative" if the count of negative words is greater, and "Neutral" if the counts are equal. The input text is assumed to be in lowercase and without punctuation.
"""

from typing import List

def sentiment_analysis(text: str, positive_words: List[str], negative_words: List[str]) -> str:
    positive_count = sum(1 for word in text.split() if word in positive_words)
    negative_count = sum(1 for word in text.split() if word in negative_words)

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"
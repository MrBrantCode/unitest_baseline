"""
QUESTION:
Write a function named `analyze_sentiment` to determine the sentiment of a given sentence, specifically whether it contains words that imply causing or likely to cause an argument, controversy, or disagreement. The function should return a descriptive string indicating the sentiment of the sentence.
"""

def analyze_sentiment(sentence):
    # List of words that imply causing or likely to cause an argument, controversy, or disagreement
    contentious_words = ["contentious", "argumentative", "controversial", "disagreement", "disagree", "argument"]

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Check if any contentious word is in the sentence
    for word in contentious_words:
        if word in sentence:
            return "The sentence contains words that imply causing or likely to cause an argument, controversy, or disagreement."

    return "The sentence does not contain words that imply causing or likely to cause an argument, controversy, or disagreement."
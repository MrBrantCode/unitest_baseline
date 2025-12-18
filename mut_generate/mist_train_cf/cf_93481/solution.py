"""
QUESTION:
Classify a sentence as either "opinionated" or "objective" based on the presence of certain opinion words or phrases. Implement a function `classify_opinionated` that takes a list of sentences as input and returns a list of corresponding classifications. The function should have a time complexity of O(n), where n is the number of sentences, and a space complexity of O(1), only storing the classification for each sentence.
"""

def classify_opinionated(sentences):
    opinion_words = ["think", "believe", "best", "worst", "love", "hate"]

    classifications = []
    for sentence in sentences:
        for word in opinion_words:
            if word in sentence.lower():
                classifications.append("opinionated")
                break
        else:
            classifications.append("objective")
    
    return classifications
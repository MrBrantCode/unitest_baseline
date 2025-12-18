"""
QUESTION:
Write a function `classify_opinionated` that takes a list of sentences as input and returns a list of classifications, where each classification is either "opinionated" or "objective". The function should achieve a time complexity of O(n), where n is the number of sentences, and a space complexity of O(1), excluding the input and output.
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
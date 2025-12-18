"""
QUESTION:
Create a function `classify_sentence` that classifies a sentence into one of three categories: question, statement, or exclamatory. The classification should be based on the punctuation at the end of the sentence. If the sentence ends with a question mark (?), it's a question. If it ends with an exclamation mark (!), it's exclamatory. If it ends with a period (.), it's a statement. If the sentence ends with any other punctuation, it should return "unknown".
"""

def classify_sentence(sentence):
    if sentence.endswith('?'):
        return "question"
    elif sentence.endswith('!'):
        return "exclamatory"
    elif sentence.endswith('.'):
        return "statement"
    else:
        return "unknown"
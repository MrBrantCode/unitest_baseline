"""
QUESTION:
Create a function `classify_sentence` that classifies a given sentence into one of seven predefined categories. The sentence will not contain punctuation marks or special characters. The list of categories is ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7'].
"""

def classify_sentence(sentence):
    categories = {
        'cat1': ['keyword1', 'keyword2'],
        'cat2': ['keyword3', 'keyword4'],
        'cat3': ['keyword5', 'keyword6'],
        'cat4': ['keyword7', 'keyword8'],
        'cat5': ['keyword9', 'keyword10'],
        'cat6': ['keyword11', 'keyword12'],
        'cat7': ['keyword13', 'keyword14']
    }

    words = sentence.lower().split()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in words:
                return category
    return 'Unknown category'
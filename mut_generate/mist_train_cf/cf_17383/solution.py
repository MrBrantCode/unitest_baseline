"""
QUESTION:
Create a function `classify_sentence` that takes a string `sentence` and a list of categories as input. Classify the given sentence into one of the categories based on the content of the sentence. The function should handle punctuation marks, special characters, and different cases of letter capitalization. Leading or trailing white spaces in the sentence should be removed before classification.
"""

def classify_sentence(sentence, categories):
    # Assuming categories is a list of tuples, where each tuple contains a category and its keywords
    # Remove leading/trailing white spaces and convert the sentence to lower case
    sentence = sentence.strip().lower()
    
    # Initialize the result as None
    result = None
    
    # Iterate over each category and its keywords
    for category, keywords in categories:
        # Check if any keyword is present in the sentence
        if any(keyword in sentence for keyword in keywords):
            # If a keyword is found, classify the sentence into the category and break the loop
            result = category
            break
    
    return result
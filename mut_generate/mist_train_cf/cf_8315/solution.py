"""
QUESTION:
Create a function named `tokenize_and_count` that takes a string sentence as input and returns a dictionary containing the word occurrences in the sentence. The function should handle punctuation marks and special characters, such as commas, periods, exclamation marks, question marks, and quotation marks. It should also handle cases where words are separated by multiple spaces or newlines. The function should not use any built-in string or list functions or data structures such as split(), count(), or dictionaries.
"""

def tokenize_and_count(sentence):
    sentence = sentence.replace("\n", " ")  # Replace newlines with spaces
    sentence = sentence.strip()  # Remove leading and trailing spaces
    occurrences = {}  # Dictionary to store the word occurrences
    
    i = 0
    while i < len(sentence):
        # Skip whitespace
        while i < len(sentence) and sentence[i] == " ":
            i += 1
        
        # Check for punctuation marks
        if sentence[i] in (".", ",", "!", "?", '"'):
            if sentence[i] in occurrences:
                occurrences[sentence[i]] += 1  # Increment occurrence count
            else:
                occurrences[sentence[i]] = 1  # Add new punctuation mark with occurrence count of 1
            i += 1
        else:
            # Find the end of the word
            j = i + 1
            while j < len(sentence) and sentence[j] not in (" ", ".", ",", "!", "?", '"'):
                j += 1
            # Extract the word and add it as token
            word = sentence[i:j]
            if word in occurrences:
                occurrences[word] += 1  # Increment occurrence count
            else:
                occurrences[word] = 1  # Add new word with occurrence count of 1
            i = j
    
    return occurrences
"""
QUESTION:
Implement a function `count_occurrences` that takes a string `sentence` as input, tokenizes it into words, and returns a dictionary with each word as a key and its occurrence count as the value. The function must handle punctuation marks (".", ",", "!", "?", '"') and special cases such as multiple spaces or newlines between words, without using built-in string or list functions or data structures like `split()`, `count()`, or dictionaries.
"""

def count_occurrences(sentence):
    # Remove leading and trailing spaces and replace newlines with spaces
    sentence = sentence.replace("\n", " ").strip()

    occurrences = {}
    i = 0
    while i < len(sentence):
        # Skip whitespace
        while i < len(sentence) and sentence[i] == " ":
            i += 1

        # Check for punctuation marks
        if sentence[i] in (".", ",", "!", "?", '"'):
            token = sentence[i]  # Add punctuation mark as token
            i += 1
        else:
            # Find the end of the word
            j = i + 1
            while j < len(sentence) and sentence[j] not in (" ", ".", ",", "!", "?", '"'):
                j += 1
            token = sentence[i:j]  # Extract the word as token
            i = j

        # Increment occurrence count
        if token in occurrences:
            occurrences[token] += 1
        else:
            occurrences[token] = 1

    return occurrences
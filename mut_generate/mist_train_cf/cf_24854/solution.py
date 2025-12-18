"""
QUESTION:
Determine the type of verb phrase in a given sentence.

Write a function called `determine_verb_phrase` that takes a sentence as input and returns the type of verb phrase involved. The function should identify the verb phrase and its type, such as simple, perfect, progressive, or perfect progressive. There are no specific restrictions on the input sentence, and the function should be able to handle various verb phrase structures.
"""

def determine_verb_phrase(sentence):
    """
    Determine the type of verb phrase in a given sentence.

    Args:
    sentence (str): The input sentence to analyze.

    Returns:
    str: The type of verb phrase involved (simple, perfect, progressive, or perfect progressive).
    """

    # Tokenize the sentence into individual words
    words = sentence.split()

    # Initialize variables to track the verb phrase type
    is_perfect = False
    is_progressive = False

    # Iterate over each word in the sentence
    for i, word in enumerate(words):
        # Check if the word is a form of "have" or "has"
        if word.lower() in ["have", "has"]:
            # Check if the next word is a past participle (e.g., "met")
            if i < len(words) - 1 and words[i + 1].endswith("ed") or words[i + 1].endswith("en"):
                is_perfect = True
        # Check if the word is a form of "be" (e.g., "is", "am", "are")
        elif word.lower() in ["is", "am", "are"]:
            # Check if the next word is a present participle (e.g., "meeting")
            if i < len(words) - 1 and words[i + 1].endswith("ing"):
                is_progressive = True

    # Determine the verb phrase type based on the flags
    if is_perfect and is_progressive:
        return "perfect progressive"
    elif is_perfect:
        return "perfect"
    elif is_progressive:
        return "progressive"
    else:
        return "simple"
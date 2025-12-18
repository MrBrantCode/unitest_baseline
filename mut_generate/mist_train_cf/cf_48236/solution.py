"""
QUESTION:
Develop a function named `transmogrify` that takes a sentence as input and returns a new sentence used for affirmation. The function should handle single words and entire phrases while maintaining the original capitalization and punctuation.
"""

def transmogrify(sentences):
    # Split the sentence into words 
    words = sentences.split()

    # Define the subject of the sentences (assumed as first word for simplicity)
    subject = words[0]

    # Create the positive assertion 
    affirmation = f"{subject} is indeed as described!"

    # Return the affirmation, maintaining the original capitalization
    return affirmation
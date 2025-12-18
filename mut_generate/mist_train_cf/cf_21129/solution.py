"""
QUESTION:
Write a function called `convert_to_imperative(sentence)` that takes a sentence as input and returns the imperative form of the sentence. The function should identify the first verb in the sentence, capitalize it, and append an exclamation mark. If the sentence does not contain a verb (identified by the suffixes 'ing' or 'ed'), return an error message.
"""

def convert_to_imperative(sentence):
    """
    Converts a sentence into its imperative form by identifying the first verb, 
    capitalizing it, and appending an exclamation mark.

    Args:
        sentence (str): The input sentence to be converted.

    Returns:
        str: The imperative form of the sentence or an error message if no verb is found.
    """
    
    # Split the sentence into words
    words = sentence.split()

    # Find the first verb in the sentence
    verb = next((word for word in words if word.endswith('ing') or word.endswith('ed')), None)

    # If no verb is found, return an error message
    if verb is None:
        return "Error: The sentence does not contain a verb."

    # Capitalize the first letter of the verb
    verb = verb.capitalize()

    # Construct the imperative sentence
    imperative_sentence = verb + '!'
    return imperative_sentence
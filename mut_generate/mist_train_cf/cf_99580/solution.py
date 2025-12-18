"""
QUESTION:
Write a function called `generate_sentences` that takes three arguments: subject, verb, and object, and returns three sentences using the present, past, and future tenses.
"""

def generate_sentences(subject, verb, object):
    """
    Generate three sentences using the present, past, and future tenses.

    Args:
    subject (str): The subject of the sentence.
    verb (str): The verb of the sentence in base form (e.g., "eat").
    object (str): The object of the sentence.

    Returns:
    list: A list of three sentences using the present, past, and future tenses.
    """
    # Generate present tense sentence
    present_tense_sentence = f"{subject} {verb}s {object} every morning."

    # Generate past tense sentence
    past_tense_sentence = f"{subject} {verb}ed {object} earlier today."

    # Generate future tense sentence
    future_tense_sentence = f"{subject} will {verb} {object} tomorrow morning."

    return [present_tense_sentence, past_tense_sentence, future_tense_sentence]
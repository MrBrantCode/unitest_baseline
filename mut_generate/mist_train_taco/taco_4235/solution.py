"""
QUESTION:
Kate likes to count words in text blocks. By words she means continuous sequences of English alphabetic characters (from a to z ). Here are examples:

`Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp.` contains "words" `['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd', 'or', 'K', 'mp']`

Kate doesn't like some of words and doesn't count them. Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.

Today Kate's too lazy and have decided to teach her computer to count "words" for her.


Example Input 1
-------------
Hello there, little user5453 374 ())$.

Example Output 1
-------------
4

Example Input 2
-------------

  I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.

Example Output 2
--------------

112
"""

from re import compile, finditer

# Set of words to be excluded
OMIT = {'a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as'}

# Regular expression to match words
REGEX = compile('[a-z]+')

def count_valid_words(text: str) -> int:
    """
    Counts the number of valid words in the given text block, excluding the specified words.

    Parameters:
    text (str): The input text block.

    Returns:
    int: The count of valid words in the text block.
    """
    # Convert the text to lowercase to ensure case-insensitive comparison
    lower_text = text.lower()
    
    # Use finditer to find all matches of the regex in the text
    matches = finditer(REGEX, lower_text)
    
    # Count the number of matches that are not in the OMIT set
    valid_word_count = sum(1 for match in matches if match.group() not in OMIT)
    
    return valid_word_count
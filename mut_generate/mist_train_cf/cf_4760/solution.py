"""
QUESTION:
Create a function called `replace_word` that takes two parameters: `text` and `word_to_replace`. The function should prompt the user for a replacement word, validate the input to ensure it's a valid word (containing only alphabets), and replace all occurrences of `word_to_replace` with the validated replacement word in the given `text`.
"""

def replace_word(text, word_to_replace):
    """
    Replace all occurrences of word_to_replace in text with a user-provided word.
    
    Args:
    text (str): The original text.
    word_to_replace (str): The word to be replaced.
    
    Returns:
    str: The modified text with word_to_replace replaced.
    """
    
    # Prompt the user for a replacement word
    replacement_word = input(f"Enter the word to replace '{word_to_replace}' with: ")
    
    # Validate the replacement word input
    while not replacement_word.isalpha():
        print("Invalid input. Please enter a valid word.")
        replacement_word = input(f"Enter the word to replace '{word_to_replace}' with: ")
    
    # Replace all occurrences of the specified word with the replacement word
    new_text = text.replace(word_to_replace, replacement_word)
    
    return new_text
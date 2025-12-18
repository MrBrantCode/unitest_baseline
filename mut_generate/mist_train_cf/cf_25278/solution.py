"""
QUESTION:
Create a function `findLongestWord` that takes two parameters: `word_dict` (a list of words) and `characters` (a set of characters). The function should return the longest word from `word_dict` that can be constructed using only the characters in `characters`. If there are multiple words of the same maximum length, return any of them.
"""

def findLongestWord(word_dict, characters):
    """
    This function takes a list of words and a set of characters as input.
    It returns the longest word from the word list that can be constructed 
    using only the characters in the set.

    Parameters:
    word_dict (list): A list of words
    characters (set): A set of characters

    Returns:
    str: The longest word that can be constructed
    """
    
    # Convert the set of characters to a list and sort it for easy comparison
    characters = sorted(list(characters))

    # Initialize the longest word and its length
    longest_word = ''
    max_length = 0

    # Iterate over each word in the word dictionary
    for word in word_dict:
        # Convert the word to a list and sort it for easy comparison
        word_list = sorted(list(word))

        # Initialize two pointers for the word and the characters
        i, j = 0, 0
        # Initialize a flag to check if the word can be constructed
        can_be_constructed = True

        # Traverse the word and the characters
        while i < len(word_list) and j < len(characters):
            # If the current character in the word is equal to the current character in the characters
            if word_list[i] == characters[j]:
                # Move to the next character in the word
                i += 1
                # Move to the next character in the characters
                j += 1
            # If the current character in the word is less than the current character in the characters
            elif word_list[i] < characters[j]:
                # The word cannot be constructed
                can_be_constructed = False
                break
            # If the current character in the word is greater than the current character in the characters
            else:
                # Move to the next character in the characters
                j += 1

        # If the word can be constructed and its length is greater than the max length
        if can_be_constructed and i == len(word_list) and len(word) > max_length:
            # Update the longest word and the max length
            longest_word = word
            max_length = len(word)

    # Return the longest word
    return longest_word
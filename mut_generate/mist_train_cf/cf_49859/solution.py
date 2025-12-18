"""
QUESTION:
Design a function named `search_word_char` that takes in three parameters: a list of strings `words`, a target word `target_word`, and a target character `target_char`. The function should perform a case-insensitive search for the target word in the list and return the index of the word and the index of the target character within that word. If the target word or character is not found, it should return a corresponding error message. The function should also handle the edge cases where the input list is empty or the target word and character do not exist.
"""

def search_word_char(words, target_word, target_char):
    try:
        # Lowercase the elements and targets to make the search case-insensitive.
        words = [word.lower() for word in words]
        target_word = target_word.lower()
        target_char = target_char.lower()

        if len(words) == 0:
            return 'The word list is empty.'
        elif target_word not in words:
            return 'The target word is not in the list.'
        else:
            word_index = words.index(target_word)
            if target_char not in target_word:
                return 'The target character is not in the target word.'
            else:
                char_index = target_word.index(target_char)
                return 'Word index: ' + str(word_index) + ', Character index: ' + str(char_index)
    except Exception as e:
        return "An error occurred: " + str(e)
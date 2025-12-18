"""
QUESTION:
Write a function `get_same_letter_words` that takes a list of strings as input and returns a list of unique substrings that consist of the same letter repeated at least 3 times, with the returned list sorted in ascending order.
"""

def get_same_letter_words(word_list):
    same_letter_words = set()
    for word in word_list:
        letters = list(word)
        for i in range(len(letters) - 2):
            for j in range(i + 2, len(letters)):
                same_letters = letters[i:j+1]
                if len(set(same_letters)) == 1:
                    same_letter_words.add(''.join(same_letters))
    return sorted(list(same_letter_words))
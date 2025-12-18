"""
QUESTION:
Construct a function `find_max_words` that takes two lists of unique string inputs as parameters. The function should return a tuple containing two words: one from each list with the most distinct characters, ignoring case. In the event of a tie, the function should return the first word alphabetically from both lists. The function must handle edge cases where one or both input lists are empty.
"""

def find_max_words(list1, list2):
    if not list1 and not list2:
        return None, None
    if not list1:
        list1.append('')
    if not list2:
        list2.append('')
    
    # For each list find a word with the maximum distinct characters
    # If there is a tie, return the lexicographically earliest word
    max_word1 = min(sorted([(len(set(word.lower())), word) for word in list1]))[1]
    max_word2 = min(sorted([(len(set(word.lower())), word) for word in list2]))[1]

    return max_word1, max_word2
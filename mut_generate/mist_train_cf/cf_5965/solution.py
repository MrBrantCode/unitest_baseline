"""
QUESTION:
Write a function `capitalize_sentence(sentence)` that capitalizes the first letter of every word in the sentence, excluding 'and' and 'the', and removes any punctuation marks at the end of each word before capitalizing it. The function should handle sentences with multiple spaces between words and punctuation marks at the end. The time complexity of the function should be O(n), where n is the length of the sentence.
"""

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        if word.lower() not in ['and', 'the']:
            word = word.rstrip(",.!?;:'")
            word = word[0].upper() + word[1:]
        capitalized_words.append(word)
    return ' '.join(capitalized_words)
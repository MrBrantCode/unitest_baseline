"""
QUESTION:
Create a function `capitalize_words` that capitalizes the first letter of each word in a given string while maintaining the original letter casing of the rest of the word. The function should ignore leading and trailing whitespace, handle multiple whitespace characters between words, and only capitalize the first letter of the alphabetic characters in words that contain numbers or special characters.
"""

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        if word.isalpha():
            capitalized_words.append(word[0].upper() + word[1:])
        else:
            for i, char in enumerate(word):
                if char.isalpha():
                    capitalized_words.append(word[:i] + word[i].upper() + word[i+1:])
                    break
            else:
                capitalized_words.append(word)
    return ' '.join(capitalized_words)
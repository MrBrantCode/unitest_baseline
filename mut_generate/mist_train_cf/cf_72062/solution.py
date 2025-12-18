"""
QUESTION:
Write a function called `remove_duplicates` that takes a string of words as input and returns the string with all duplicate words removed. The function should be case-insensitive when comparing words for duplicates, but it should preserve the original case of the words in the output string. The function should not use any built-in string or array manipulation functions.
"""

def remove_duplicates(sentence):
    result = ""
    seen = []
    word = ""

    for ch in sentence:
        if ch == " ":
            if word.lower() not in seen:
                seen.append(word.lower())
                if result == "":
                    result += word
                else:
                    result += " " + word
            word = ""
        else:
            word += ch

    # add the last word
    if word.lower() not in seen:
        if result == "":
            result += word
        else:
            result += " " + word

    return result
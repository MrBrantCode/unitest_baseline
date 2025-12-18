"""
QUESTION:
Create a function named `convert_to_italics` that takes a sentence as input and returns the sentence with the first occurrence of the word 'bold' (case-insensitive) converted to italics in HTML format, i.e., surrounded by `<i>` and `</i>` tags, while leaving other occurrences of 'bold' unchanged.
"""

def convert_to_italics(sentence):
    words = sentence.split()
    modified_words = []
    found_bold = False

    for word in words:
        if word.lower() == 'bold' and not found_bold:
            modified_words.append('<i>' + word + '</i>')
            found_bold = True
        else:
            modified_words.append(word)

    updated_sentence = ' '.join(modified_words)
    return updated_sentence
"""
QUESTION:
Write a function `generate_sentence(words, pos_tags)` that takes a list of words and their corresponding parts of speech tags as input and returns a new sentence with the words rearranged to be grammatically correct. The function should handle the following parts of speech: nouns (N), verbs (V), adjectives (J), adverbs (R), determiners (D), and prepositions (P).
"""

def generate_sentence(words, pos_tags):
    sentence = ""
    for word, pos in zip(words, pos_tags):
        if pos.startswith('N'):  # Noun
            sentence += "a " + word + " "
        elif pos.startswith('V'):  # Verb
            sentence += "to " + word + " "
        elif pos.startswith('J'):  # Adjective
            sentence += "very " + word + " "
        elif pos.startswith('R'):  # Adverb
            sentence += "quickly " + word + " "
        elif pos.startswith('D'):  # Determiner
            sentence += "the " + word + " "
        elif pos.startswith('P'):  # Preposition
            sentence += "in " + word + " "
        else:
            sentence += word + " "

    return sentence.strip()
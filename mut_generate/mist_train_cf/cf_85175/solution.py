"""
QUESTION:
Create a function `filter_words` that takes a sentence and a list of prepositions and conjunctions as input, and returns a list of words in the sentence excluding the given prepositions and conjunctions in reverse order.
"""

def filter_words(sentence, prepositions_conjunctions):
    return [word for word in sentence.split() if word not in prepositions_conjunctions][::-1]
"""
QUESTION:
Write a function `count_alphabets` that takes a list of strings `lexemes` as input and returns a dictionary where the keys are the alphabets present in the strings and the values are their respective occurrence rates. The function should disregard case disparities and ignore non-alphabetic symbols and numerals.
"""

def count_alphabets(lexemes):
    occurrence_rate = dict()
    for lexeme in lexemes:
        for character in lexeme:
            if character.isalpha():
                character = character.lower()
                if character not in occurrence_rate:
                    occurrence_rate[character] = 1
                else:
                    occurrence_rate[character] += 1
    return occurrence_rate
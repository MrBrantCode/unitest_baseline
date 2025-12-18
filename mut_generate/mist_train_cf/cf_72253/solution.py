"""
QUESTION:
Create a function `switch_case(input_string)` that processes a given string by splitting it into words and using a dictionary-based case structure to map each word to a corresponding value. The function should return a list of values corresponding to the words in the input string, and return "Not Defined" if a word does not have a corresponding value in the case structure. The input string is case-sensitive.
"""

def switch_case(input_string):
    case_dict = {"Felis":"Species", "catus":"Genus"}

    words = input_string.split() 
    result = []
    for word in words:
        result.append(case_dict.get(word, "Not Defined")) 

    return result
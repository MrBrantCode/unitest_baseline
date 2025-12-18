"""
QUESTION:
Create a function called `lexemes_positions` that takes a string of text as input and returns a multilevel dictionary. The dictionary should contain lexemes (words) from the text that have more than 5 characters. Each lexeme should be a key in the dictionary, with its corresponding value being another dictionary containing the count of the lexeme and a list of its positions in the text. The lexemes dictionary should be wrapped under the key 'Level1'. The position index should start from 0 and only consider words with more than 5 characters.
"""

def lexemes_positions(text):
    """
    This function generates a multilevel dictionary filled with lexemes 
    exceeding a string length of five and also provides the count of 
    individual lexemes at each level and their respective position in the syntax.
    """
    
    words = text.split()
    lexemes = [word for word in words if len(word) > 5]
    lexemes_positions = {}
    for i, lexeme in enumerate(lexemes):
        if lexeme not in lexemes_positions:
            lexemes_positions[lexeme] = {"count": 1, "positions": [i]}
        else:
            lexemes_positions[lexeme]["count"] += 1
            lexemes_positions[lexeme]["positions"].append(i)
    
    lexemes_dict = {"Level1": lexemes_positions}
    
    return lexemes_dict
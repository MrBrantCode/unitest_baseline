"""
QUESTION:
Write a function `lexical_analysis` that performs lexical analysis on a given Python code snippet. The function should break down the source code into a sequence of tokens, which are meaningful units of the programming language such as keywords, identifiers, operators, and literals. The function should identify and categorize different elements of the programming language, scanning the source code character by character, removing unnecessary white spaces and comments, and identifying the structure of the program.
"""

def lexical_analysis(code):
    keywords = ['def', 'return', 'print']
    operators = ['+', '-', '*', '/', '=', '(', ')', ':', ',']
    tokens = []
    word = ''

    for char in code:
        if char.isspace():
            if word:
                if word in keywords:
                    tokens.append(('keyword', word))
                elif word.isdigit():
                    tokens.append(('literal', word))
                else:
                    tokens.append(('identifier', word))
                word = ''
        elif char in operators:
            if word:
                if word in keywords:
                    tokens.append(('keyword', word))
                elif word.isdigit():
                    tokens.append(('literal', word))
                else:
                    tokens.append(('identifier', word))
                word = ''
            tokens.append(('operator', char))
        else:
            word += char

    if word:
        if word in keywords:
            tokens.append(('keyword', word))
        elif word.isdigit():
            tokens.append(('literal', word))
        else:
            tokens.append(('identifier', word))

    return tokens
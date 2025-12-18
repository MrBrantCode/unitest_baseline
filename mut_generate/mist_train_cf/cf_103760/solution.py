"""
QUESTION:
Write a function named `translate_to_machine_code` that takes a high-level programming language source code as input and translates it into machine code. The function should perform the following stages: lexical analysis, syntax analysis, semantic analysis, code optimization, and code generation. Assume the input source code is a string and the machine code is represented as a string. The function should return the translated machine code as a string.
"""

def translate_to_machine_code(source_code):
    # Lexical Analysis
    tokens = []
    keywords = ["if", "else", "for", "while", "class", "def"]
    operators = ["+", "-", "*", "/", "="]
    for line in source_code.splitlines():
        for word in line.split():
            if word in keywords:
                tokens.append(("keyword", word))
            elif word in operators:
                tokens.append(("operator", word))
            else:
                tokens.append(("identifier", word))

    # Syntax Analysis
    syntax_tree = []
    for token in tokens:
        if token[0] == "keyword":
            syntax_tree.append(token[1])

    # Semantic Analysis
    symbol_table = {}
    for token in tokens:
        if token[0] == "identifier":
            symbol_table[token[1]] = "variable"

    # Code Optimization
    optimized_code = []
    for token in syntax_tree:
        if token == "if":
            optimized_code.append(token)

    # Code Generation
    machine_code = ""
    for token in optimized_code:
        machine_code += token + "\n"

    return machine_code
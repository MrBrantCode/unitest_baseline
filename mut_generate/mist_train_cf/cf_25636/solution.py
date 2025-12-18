"""
QUESTION:
Write a function to generate a context-free grammar that produces strings consisting only of 'a's and 'b's with an equal number of 'a's and 'b's.
"""

def generate_context_free_grammar(n):
    grammar = "S -> "
    for i in range(n):
        grammar += "bAa"
    grammar += " | "
    grammar += "A -> AaA | aAa | bAb | abB | ε"
    return grammar
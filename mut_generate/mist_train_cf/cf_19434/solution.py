"""
QUESTION:
Write a function `classify_sentence` that classifies a given sentence as a declaration or an instruction. The function should be able to handle sentences with multiple clauses, nested clauses, and various punctuation marks.
"""

def classify_sentence(sentence):
    # Remove leading and trailing whitespace
    sentence = sentence.strip()
    
    # Remove all punctuation
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace())
    
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Split the sentence into clauses
    clauses = sentence.split(',')
    
    # Check if the sentence is an instruction
    instruction_indicators = ['should', 'can', 'must', 'will', 'shall', 'may', 'might', 'could', 'would', 'ought to']
    for clause in clauses:
        for word in instruction_indicators:
            if word in clause:
                return 'instruction'
    
    # If no instruction indicators are found, it's a declaration
    return 'declaration'
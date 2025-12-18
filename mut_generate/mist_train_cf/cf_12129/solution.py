"""
QUESTION:
Classify a given sentence as either a declaration or an instruction. The sentence may contain multiple clauses and punctuation marks. Develop a function named `classify_sentence` to perform this task.
"""

def classify_sentence(sentence):
    if sentence.strip()[-1] == '.':
        return "Declaration"
    else:
        return "Instruction"
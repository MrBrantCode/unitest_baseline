"""
QUESTION:
Write a Python function `solve_word_analogy(A, B, C, ts_constraint)` that solves a word analogy puzzle with the given constraint. The function should receive four arguments: A, B, C, and the reversed 'ts' constraint (`ts_constraint`). The function should find the missing word that completes the analogy "A is to B as C is to ____" with the additional constraint that the missing word must contain the letters 't' and 's' in reverse order (`ts_constraint`).
"""

def solve_word_analogy(A, B, C, ts_constraint):
    for word in [A, B, C]:
        if ts_constraint in word:
            ts_index = word.index(ts_constraint)
            break
    else:
        return "No solution found"
    
    for word in [A, B, C]:
        if word != A and word != B and word != C and word[ts_index:ts_index+2] == ts_constraint[::-1]:
            return word
    
    return "No solution found"
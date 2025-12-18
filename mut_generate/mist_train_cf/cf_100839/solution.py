"""
QUESTION:
Write a function `solve_word_analogy(A, B, C, ts_constraint)` that solves a word analogy puzzle where the missing word must contain the letters 't' and 's' in reverse order. The function receives four arguments: A, B, C, and the reversed 'ts' constraint, and returns the missing word that completes the analogy.
"""

def entrance(A, B, C, ts_constraint):
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
"""
QUESTION:
Write a function named `solve_word_analogy(A, B, C, ts_constraint)` that takes four arguments: A, B, C, and ts_constraint. The function should solve a word analogy puzzle where A is to B as C is to ____, with the constraint that the missing word must contain the letters 't' and 's' in reverse order (i.e., 'st'). Return the missing word that completes the analogy. If no solution is found, return "No solution found".
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
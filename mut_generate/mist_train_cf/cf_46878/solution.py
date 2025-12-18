"""
QUESTION:
Implement a function `levenshtein(src, tgt)` that calculates the minimum number of insertions, deletions, and substitutions required to change the string `src` into the string `tgt`. The function should consider the sequence of characters, including words, punctuation, and white spaces, and should be optimized for longer text inputs. The function should return the minimum number of edits required to convert `src` into `tgt`.
"""

def levenshtein(src, tgt):
    if len(src) < len(tgt):
        return levenshtein(tgt, src)

    if len(tgt) == 0:
        return len(src)

    previous_row = range(len(tgt) + 1)
    for i, src_char in enumerate(src):
        current_row = [i + 1]
        for j, tgt_char in enumerate(tgt):
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1  
            substitutions = previous_row[j] + (src_char != tgt_char)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]
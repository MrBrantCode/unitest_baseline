"""
QUESTION:
Write a function `check_permutations(seq1, seq2)` that determines whether two given character sequences are permutations of each other. The function should return a boolean value indicating whether the sequences are permutations, and two lists containing the index and character where the sequences first diverge. If the sequences are permutations but identical, the function should return two empty lists. The function should accommodate for special characters and spaces, and assume index starts from 0.
"""

def check_permutations(seq1, seq2):
    if sorted(seq1) == sorted(seq2): 
        for i in range(len(seq1)):  
            if seq1[i] != seq2[i]:  
                return True, [i, seq1[i]], [i, seq2[i]]  
        return True, [], []  
    else:  
        for i in range(min(len(seq1), len(seq2))):  
            if seq1[i] != seq2[i]:  
                return False, [i, seq1[i]], [i, seq2[i]]  
        return False, [len(seq2), ''] if len(seq1)>len(seq2) else [len(seq1), ''],\
            [max(len(seq2),len(seq1))-1,seq2[-1] if len(seq2)>len(seq1) else seq1[-1]]
"""
QUESTION:
Construct a context-free grammar to describe the language {anbmcn | n, m ≥ 1}, where each 'a' is followed by 'b' and then 'c', the number of 'a's is equal to the number of 'b's which is equal to the number of 'c's, the number of 'a's is greater than the number of 'b's, and the number of 'b's is greater than the number of 'c's. The grammar should not allow consecutive 'a's, 'b's, or 'c's and the number of 'a's should be divisible by 3.
"""

def check_string(s):
    a_count = s.count('a')
    b_count = s.count('b')
    c_count = s.count('c')
    
    if a_count % 3 != 0 or a_count <= b_count or b_count <= c_count:
        return False
    
    if 'aa' in s or 'bb' in s or 'cc' in s:
        return False
    
    return a_count == b_count == c_count
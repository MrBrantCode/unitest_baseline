"""
QUESTION:
Construct a context-free grammar (CFG) for the language {anbmcn | n, m ≥ 0} where each 'a' is followed by 'b' and then 'c', the number of 'a's equals the number of 'b's equals the number of 'c's, the number of 'a's is greater than or equal to the number of 'b's, and the number of 'b's is greater than or equal to the number of 'c's. The grammar should not allow consecutive 'a's, 'b's, or 'c's.
"""

def entrance(s):
    stack = []
    num_a, num_b, num_c = 0, 0, 0
    for char in s:
        if char == 'a':
            num_a += 1
            if stack and stack[-1] == 'a':
                return False
            stack.append(char)
        elif char == 'b':
            num_b += 1
            if stack and stack[-1] == 'b':
                return False
            stack.append(char)
        elif char == 'c':
            num_c += 1
            if stack and stack[-1] == 'c':
                return False
            stack.append(char)
        else:
            return False
    return num_a == num_b == num_c and num_a >= num_b >= num_c
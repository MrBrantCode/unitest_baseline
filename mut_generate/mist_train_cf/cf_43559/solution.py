"""
QUESTION:
Given a string `S` of lowercase letters and an integer `K`, remove all sequences of `K` adjacent and equal letters from `S` until no more such sequences exist. The function should return the final string after all such duplicate removals have been made. 

The input string `S` is guaranteed to be 1 to 20000 characters long, consisting only of English lowercase letters. The integer `K` is between 1 and the length of `S`.
"""

def entrance(S: str, K: int) -> str:
    stack = []
    for c in S:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == K:
                stack.pop()
        else:
            stack.append([c, 1])
            
    return ''.join(c * k for c, k in stack)
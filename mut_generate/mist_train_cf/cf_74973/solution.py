"""
QUESTION:
Given a string `s` of length between 1 and 10^4, consisting only of lowercase English letters, write a function `removeDuplicateLetters(s)` that removes duplicate letters so that every letter appears once and only once, and rearranges the remaining letters in lexicographical order. The function should also ensure that no two same letters are adjacent to each other. If it is not possible to rearrange the letters in such a way, return an empty string.
"""

def removeDuplicateLetters(s: str) -> str:
    last_occurrence = {c: i for i, c in enumerate(s)}
    stack = []
    in_stack = set()
    
    for i, c in enumerate(s):
        if c not in in_stack:
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                in_stack.remove(stack.pop())
            stack.append(c)
            in_stack.add(c)
    
    return ''.join(stack)
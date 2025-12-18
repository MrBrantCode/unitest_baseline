"""
QUESTION:
Create a function `findMaxValid` that takes a string `s` as input and returns the length of the longest valid (well-formed) parentheses substring. The input string may contain special characters and integers in addition to parentheses. The function should be efficient and follow best coding practices.
"""

def findMaxValid(s): 
    stack = [] 
    result = 0
    base = -1

    for i in range(len(s)): 
        if s[i] == '(': 
            stack.append(i) 
        else: 
            if len(stack) == 0: 
                base = i 
            else: 
                stack.pop() 
                if len(stack) == 0: 
                    result = max(result, i - base) 
                else: 
                    result = max(result, i - stack[len(stack)-1]) 
    return result 
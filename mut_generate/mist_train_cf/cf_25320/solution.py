"""
QUESTION:
Write a function `minWindow(s, t)` that finds the minimum window in string `s` which contains all characters in string `t`. The function should return the length of the minimum window.
"""

def minWindow(s, t): 
    minWindowLength = None
    leftIndex = 0 
    balance = {}
    for char in t:
        if char not in balance:
            balance[char] = 1
        else:
            balance[char] += 1
    leftIndex = 0
    rightIndex = 0
    charactersFound = 0
    for i in range(len(s)): 
        if s[i] in balance: 
            balance[s[i]] -= 1  
            if balance[s[i]] == 0: 
                charactersFound += 1
        if charactersFound == len(balance): 
            while(rightIndex <= i and charactersFound == len(balance)): 
                if s[leftIndex] in balance: 
                    if balance[s[leftIndex]] == 0: 
                        charactersFound -= 1
                    balance[s[leftIndex]] += 1
                if minWindowLength == None or (i-leftIndex+1) < minWindowLength: 
                    minWindowLength = i-leftIndex+1
                leftIndex += 1
    return minWindowLength
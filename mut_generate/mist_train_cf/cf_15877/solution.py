"""
QUESTION:
Create a function `permute_unique` that prints all unique permutations of a given string. The string may contain duplicate characters. The function should have a time complexity of O(n!) and a space complexity of O(n!).
"""

def permute_unique(string):
    def backtrack(start):
        if start == len(string):
            result.append(''.join(string))
        seen = set()  
        for i in range(start, len(string)):
            if string[i] in seen:
                continue  
            seen.add(string[i])
            string[start], string[i] = string[i], string[start]  
            backtrack(start + 1)
            string[start], string[i] = string[i], string[start]  

    result = []
    string = list(string)
    backtrack(0)
    return result
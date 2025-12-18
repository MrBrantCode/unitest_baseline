"""
QUESTION:
Create a function `get_unique_combinations` that takes a string of characters as an argument and returns a list of all unique combinations of characters possible, excluding any combination that includes a repeating character. The function should have a time complexity of O(2^n), where n is the length of the input string.
"""

def get_unique_combinations(string):
    def backtrack(comb, start):
        res.append(comb)
        for i in range(start, len(string)):
            if i > start and string[i] == string[i-1]:
                continue
            backtrack(comb + string[i], i + 1)
    
    res = []
    string = ''.join(sorted(string))
    backtrack("", 0)
    return res
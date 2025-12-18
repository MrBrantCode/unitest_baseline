"""
QUESTION:
Create a function `permute_unique` that prints all unique permutations of a given string, handling duplicate characters. The function should have a time complexity of O(n!) and a space complexity of O(n!).
"""

def permute_unique(string):
    def backtrack(start):
        if start == len(string):
            result.append(''.join(string))
        seen = set()  # Track seen characters at each level
        for i in range(start, len(string)):
            if string[i] in seen:
                continue  # Skip duplicate characters
            seen.add(string[i])
            string[start], string[i] = string[i], string[start]  # Swap
            backtrack(start + 1)
            string[start], string[i] = string[i], string[start]  # Backtrack (undo the swap)

    result = []
    string = list(string)
    backtrack(0)
    return result
"""
QUESTION:
Implement a function `combinations(s: str) -> List[str]` that finds all possible combinations of a given string and returns them as a list of strings. The order of the combinations does not matter. The function should return an empty string as one of the combinations.
"""

from typing import List

def combinations(s: str) -> List[str]:
    if len(s) == 0:
        return [""]  
    else:
        result = []
        for i in range(len(s)):
            char = s[i]
            remaining = s[:i] + s[i+1:]  
            subcombinations = combinations(remaining)  
            for combination in subcombinations:
                result.append(combination)
                result.append(char + combination)  
        return result
"""
QUESTION:
Create a function `get_combinations` that generates an array of strings containing all possible combinations of n characters from a given string of characters. The order of the characters in each string must be lexicographically sorted, and the function must handle cases where the given string contains duplicate characters. Optimize the solution to have a time complexity better than O(2^n).
"""

from collections import Counter

def get_combinations(string, n):
    counter = Counter(string)
    unique_chars = sorted(set(string))
    combinations = []
    
    def backtrack(current_combination, remaining_chars, remaining_length):
        if remaining_length == 0:
            combinations.append("".join(current_combination))
            return
        
        for char in remaining_chars:
            if counter[char] == 0:
                continue
            current_combination.append(char)
            counter[char] -= 1
            backtrack(current_combination, remaining_chars, remaining_length - 1)
            current_combination.pop()
            counter[char] += 1
    
    backtrack([], unique_chars, n)
    return combinations
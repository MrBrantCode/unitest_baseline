"""
QUESTION:
Write a function `find_combinations(string)` that generates all possible combinations of the characters in a given string. The function should return a list of all possible combinations and have a time complexity of O(n!).
"""

def find_combinations(string):
    def generate_combinations(prefix, remaining, combinations):
        if len(remaining) == 0:
            combinations.append(prefix)
        else:
            for i in range(len(remaining)):
                generate_combinations(prefix + remaining[i], remaining[:i] + remaining[i+1:], combinations)

    combinations = []
    generate_combinations("", string, combinations)
    return combinations
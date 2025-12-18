"""
QUESTION:
Write a function `find_combinations` that takes a string `string` as input and returns all possible combinations of the string's characters. The time complexity of the solution should be O(n!).
"""

def find_combinations(string):
    combinations = []
    def generate_combinations(prefix, remaining):
        if len(remaining) == 0:
            combinations.append(prefix)
        else:
            for i in range(len(remaining)):
                generate_combinations(prefix + remaining[i], remaining[:i] + remaining[i+1:])
    generate_combinations("", string)
    return combinations
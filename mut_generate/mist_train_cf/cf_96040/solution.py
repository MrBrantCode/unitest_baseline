"""
QUESTION:
Write a function named `find_combinations_reverse` that generates all possible combinations of a given string and returns them in reverse order. The function should have a time complexity of O(n^2 * n!), where n is the length of the string. The function should not take any additional arguments other than the input string.
"""

def entrance(string):
    combinations = []

    def generate_combinations(substring, prefix):
        if len(substring) == 0:
            combinations.append(prefix[::-1])
        else:
            for i in range(len(substring)):
                char = substring[i]
                generate_combinations(substring[:i] + substring[i+1:], prefix + char)

    generate_combinations(string, "")
    return combinations
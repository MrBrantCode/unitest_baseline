"""
QUESTION:
Write a function named `countPatternCombinations` that takes a string `expression` as input and returns the count of combinations of the pattern '00' within the string. The pattern is a sequence of two characters '0' where the characters must be adjacent to each other in the string. The function should only consider the input string and return the total count of the '00' pattern combinations.
"""

def countPatternCombinations(expression):
    combinations = 0
    for i in range(len(expression) - 1):
        if expression[i:i+2] == '00':
            combinations += 1
    return combinations
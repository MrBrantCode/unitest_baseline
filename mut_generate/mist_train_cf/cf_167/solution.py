"""
QUESTION:
Implement a function `calculate_big_o(algorithm)` that calculates the Big O notation for a given algorithm's time complexity. The algorithm is a string that represents a Python code snippet, and may contain recursive calls and nested loops. The function should return a string representation of the Big O notation.
"""

def calculate_big_o(algorithm):
    algorithm = algorithm.strip()
    if algorithm == "":
        return "O(1)"
    if algorithm.startswith("for") or algorithm.startswith("while"):
        return "O(n)"
    if algorithm.startswith("if"):
        nested_big_o = calculate_big_o(algorithm[algorithm.find(":") + 1 :])
        return nested_big_o
    if algorithm.startswith("for") and algorithm[algorithm.find(":") + 1 :].find("for") != -1:
        nested_big_o = calculate_big_o(algorithm[algorithm.find(":") + 1 :])
        return f"O(n * {nested_big_o})"
    return "Unknown"
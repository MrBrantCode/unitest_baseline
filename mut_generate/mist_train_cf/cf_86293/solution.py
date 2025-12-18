"""
QUESTION:
Implement a function named `calculate_big_o` that takes a string representing a Python algorithm as input. The function should analyze the algorithm's time complexity by considering recursive and iterative approaches, as well as nested loops. It should return a string representation of the algorithm's Big O notation.
"""

def calculate_big_o(algorithm):
    algorithm = algorithm.strip()  # Remove leading/trailing whitespaces
    if algorithm == "":
        return "O(1)"  # If the algorithm has no operations, it is constant time

    if algorithm.startswith("for") or algorithm.startswith("while"):
        return "O(n)"  # If the algorithm contains a single loop, it is linear time

    if algorithm.startswith("if"):
        nested_big_o = calculate_big_o(algorithm[algorithm.find(":") + 1 :])  # Recursive call for nested part
        return nested_big_o  # The overall time complexity is the same as the nested part

    if algorithm.startswith("for") and algorithm[algorithm.find(":") + 1 :].find("for") != -1:
        nested_big_o = calculate_big_o(algorithm[algorithm.find(":") + 1 :])  # Recursive call for nested part
        return f"O(n * {nested_big_o})"  # The overall time complexity is the product of the two loops

    return "Unknown"  # If the algorithm doesn't match any known patterns, return "Unknown"
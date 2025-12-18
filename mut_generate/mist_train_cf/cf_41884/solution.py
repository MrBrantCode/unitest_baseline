"""
QUESTION:
Write a function `combine_elements(commands: str) -> List[List[int]]` that takes a string of space-separated commands as input, where each command starts with "-St " followed by a comma-separated list of numbers in increasing order. Return a list of combined elements, where each element is a list of numbers from a command. If the input string is empty, return an empty list.
"""

from typing import List

def combine_elements(commands: str) -> List[List[int]]:
    if not commands:
        return []

    combined_elements = []
    commands_list = commands.split("-St ")[1:]
    for command in commands_list:
        numbers = [int(num) for num in command.split(",")]
        combined_elements.append(numbers)

    return combined_elements
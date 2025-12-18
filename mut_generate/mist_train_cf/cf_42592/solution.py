"""
QUESTION:
Implement a function `countCommands` that takes a list of strings representing module/action pairs in the format "module/action" and returns a dictionary where the keys are the unique pairs and the values are the counts of each pair in the input list. The input list contains no invalid or malformed module/action pairs. The function should be able to handle an empty input list.
"""

from typing import List, Dict

def countCommands(commands: List[str]) -> Dict[str, int]:
    command_counts = {}
    for command in commands:
        if command in command_counts:
            command_counts[command] += 1
        else:
            command_counts[command] = 1
    return command_counts
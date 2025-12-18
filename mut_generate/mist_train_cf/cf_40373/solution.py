"""
QUESTION:
Write a function `parse_code_snippet(code_snippet: str) -> List[Tuple[int, str, str, str]]` that takes a string `code_snippet` representing a code snippet where each line is in the format `<line_number> <action_type> <action_name> <action_details>`. Return a list of tuples, where each tuple contains the line number, action type, action name, and action details extracted from the code snippet. The function should handle action details that may contain alphanumeric characters and special characters.
"""

from typing import List, Tuple

def entance(code_snippet: str) -> List[Tuple[int, str, str, str]]:
    parsed_actions = []
    lines = code_snippet.strip().split('\n')
    for line in lines:
        parts = line.split()
        if len(parts) > 3:
            line_number = int(parts[0])
            action_type = parts[1]
            action_name = parts[2]
            action_details = ' '.join(parts[3:])
            parsed_actions.append((line_number, action_type, action_name, action_details))
    return parsed_actions
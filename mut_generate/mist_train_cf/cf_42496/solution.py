"""
QUESTION:
Implement a function `process_scene_script` that takes a string `script` as input and returns a list of tuples, where each tuple contains the name of the object and the action performed on it. The script contains function calls and comments. Each function call represents an action on an object, and comments are ignored. The function should extract the object name and action from each function call and return the result as a list of tuples. The script length is between 1 and 1000 characters.
"""

from typing import List, Tuple

def process_scene_script(script: str) -> List[Tuple[str, str]]:
    objects_actions = []
    lines = script.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            parts = line.split('(')
            if len(parts) > 1:
                action = parts[0].split('.')[-1]
                obj = parts[1].split(',')[0].strip().strip('"')
                objects_actions.append((obj, action))
    return objects_actions
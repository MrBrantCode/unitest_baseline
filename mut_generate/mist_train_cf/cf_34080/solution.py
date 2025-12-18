"""
QUESTION:
Create a function `execute_startup_scripts` that takes a list of script names as input and returns a list of scripts that should be executed based on the following rules:
- The script name starts with "start_".
- The script name ends with ".sh".
- The script name contains the string "unum".
A script should be executed if it meets any of these criteria, and it should only appear once in the output list.
"""

from typing import List

def execute_startup_scripts(script_names: List[str]) -> List[str]:
    executed_scripts = set()
    result = []
    for script in script_names:
        if script.startswith("start_") or script.endswith(".sh") or "unum" in script:
            if script not in executed_scripts:
                result.append(script)
                executed_scripts.add(script)
    return result
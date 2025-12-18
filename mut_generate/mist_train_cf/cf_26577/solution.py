"""
QUESTION:
Implement a function `resolveConflicts` that takes a list of input configurations and returns a list of resolved input configurations, ensuring that no conflicting configurations are active simultaneously. Each input configuration is a dictionary with "subcategory", "allowedconflicts", and "mode" keys. Resolve conflicts based on the following rules: 
1. Two input configurations with the same subcategory and mode are considered conflicting.
2. If an input configuration A has B in its allowedconflicts list, and B is active, A cannot be active.
If conflicts cannot be resolved, return an empty list.

Input: A list of dictionaries, where each dictionary has the following keys: 
- "subcategory": a string representing the subcategory of the input configuration
- "allowedconflicts": a list of strings representing the subcategories of input configurations that cannot be active simultaneously with the current one
- "mode": a string representing the operating mode of the input configuration

Output: A list of resolved input configurations, ensuring that no conflicting configurations are active simultaneously.
"""

from typing import List, Dict, Union

def resolveConflicts(configs: List[Dict[str, Union[str, List[str]]]]) -> List[Dict[str, Union[str, List[str]]]]:
    active_configs = []
    resolved_configs = []

    for config in configs:
        conflicts = [c for c in active_configs if c["subcategory"] in config["allowedconflicts"]]
        if not conflicts:
            active_configs.append(config)
            resolved_configs.append(config)
        else:
            conflicting_modes = [c for c in conflicts if c["mode"] == config["mode"]]
            if conflicting_modes:
                continue
            else:
                active_configs.append(config)
                resolved_configs.append(config)

    return resolved_configs
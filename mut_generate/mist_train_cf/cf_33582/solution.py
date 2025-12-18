"""
QUESTION:
Implement a function `extract_network_devices(commands: List[str]) -> List[str]` that takes a list of Linux `ip` utility commands as input, extracts the names of network devices being manipulated, and returns them as a list of unique strings. The input commands may contain comments denoted by the `#` symbol and should be ignored. The function should only consider lines starting with the `ip` keyword and extract device names following the `dev` keyword.
"""

from typing import List

def extract_network_devices(commands: List[str]) -> List[str]:
    device_names = set()
    for command in commands:
        if command.strip().startswith("ip") and "#" not in command:
            parts = command.split()
            for part in parts:
                if part == "dev" and len(parts) > parts.index(part) + 1:
                    device_names.add(parts[parts.index(part) + 1])
    return list(device_names)
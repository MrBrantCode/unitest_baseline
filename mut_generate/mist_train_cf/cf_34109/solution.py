"""
QUESTION:
Write a function `extract_file_copies(json_config, os_condition, arch_condition)` that takes in a JSON configuration, an operating system condition, and a target architecture condition as input and returns a list of tuples containing the destination directory and the list of files for the matching configurations. The JSON configuration is a dictionary with a "copies" key that contains a list of dictionaries, each representing a configuration with a "conditions" key and a "copies" key. The "conditions" key contains a string representing a Python condition, and the "copies" key contains a list of dictionaries, each representing a file copy with "destination" and "files" keys. The function should evaluate the condition using the provided `os_condition` and `arch_condition` and return the destination directory and list of files for matching configurations. If no matching configurations are found, the function should return an empty list.
"""

from typing import List, Tuple

def extract_file_copies(json_config: dict, os_condition: str, arch_condition: str) -> List[Tuple[str, List[str]]]:
    matching_copies = []
    for copy in json_config.get("copies", []):
        conditions = copy.get("conditions", "")
        if eval(conditions, {"OS": os_condition, "target_arch": arch_condition}):
            for file_copy in copy.get("copies", []):
                destination = file_copy.get("destination", "")
                files = file_copy.get("files", [])
                matching_copies.append((destination, files))
    return matching_copies
"""
QUESTION:
Implement the `version_control(commands)` function that takes a list of commands as input and returns a dictionary representing the final state of the files after executing the commands. The keys of the dictionary are the file names, and the values are lists containing the versions of the file in chronological order. Each command is either "commit <file_name>" or "checkout <file_name> <version>". The function should create a new version of the file when a "commit" command is executed and revert the file to a specified version when a "checkout" command is executed if the version exists.
"""

from typing import List, Dict

def version_control(commands: List[str]) -> Dict[str, List[str]]:
    file_versions = {}
    
    for command in commands:
        action, *args = command.split()
        if action == "commit":
            file_name = args[0]
            if file_name not in file_versions:
                file_versions[file_name] = [f"{file_name}_v1"]
            else:
                latest_version = file_versions[file_name][-1]
                version_number = int(latest_version.split("_v")[1]) + 1
                file_versions[file_name].append(f"{file_name}_v{version_number}")
        elif action == "checkout":
            file_name, version = args
            if file_name in file_versions and int(version) <= len(file_versions[file_name]):
                file_versions[file_name] = file_versions[file_name][:int(version)]
    
    return file_versions
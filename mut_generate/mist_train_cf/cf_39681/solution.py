"""
QUESTION:
Write a function named `execute_commands` that takes a list of strings as input, where each string represents a command. The function should return a list of strings representing the order in which the commands are executed. The function must execute the "cargo doc" command immediately when encountered and execute the "rustup component add rustfmt-preview" command only if the "cargo doc" command has been previously executed.
"""

from typing import List

def execute_commands(commands: List[str]) -> List[str]:
    executed_commands = []
    cargo_doc_executed = False

    for command in commands:
        if command == "cargo doc":
            executed_commands.append(command)
            cargo_doc_executed = True
        elif command == "rustup component add rustfmt-preview":
            if cargo_doc_executed:
                executed_commands.append(command)
            else:
                # Handle the case where rustfmt-preview is added before cargo doc
                pass

    return executed_commands
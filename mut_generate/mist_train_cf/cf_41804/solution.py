"""
QUESTION:
Write a function `process_sql_commands` that takes two parameters: `sql_commands`, a string of SQL commands separated by semicolons, and `substitutions`, a list of tuples containing search and replacement strings. The function should split the SQL commands into individual commands, apply the substitutions to each command, and return the modified commands as a single string separated by semicolons. Each tuple in the `substitutions` list specifies a search string and a replacement string.
"""

from typing import List, Tuple

def process_sql_commands(sql_commands: str, substitutions: List[Tuple[str, str]]) -> str:
    modified_commands = []
    
    # Split the SQL commands based on semicolon delimiter
    commands = sql_commands.split(';')
    
    for command in commands:
        modified_command = command
        # Apply substitutions for each command
        for substitution in substitutions:
            search_str, replace_str = substitution
            modified_command = modified_command.replace(search_str, replace_str)
        modified_commands.append(modified_command)
    
    # Join the modified commands with semicolons and return as a single string
    return ';'.join(modified_commands)
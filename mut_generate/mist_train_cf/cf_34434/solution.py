"""
QUESTION:
Implement the `process_migration_commands` function, which takes a list of migration commands as input and returns a list of processed commands in the correct order. The processed commands should be in the format of `(command_type, table_name, index_or_column_name)`. The function should support two types of commands: `op.drop_index(index_name, table_name)` and `op.drop_column(column_name, table_name)`.
"""

from typing import List, Tuple

def process_migration_commands(commands: List[str]) -> List[Tuple[str, str, str]]:
    processed_commands = []
    for command in commands:
        if "op.drop_index" in command:
            index_name = command.split("op.f('")[1].split("')")[0]
            table_name = command.split("table_name='")[1].split("'")[0]
            processed_commands.append(('drop_index', table_name, index_name))
        elif "op.drop_column" in command:
            table_name = command.split("('")[1].split("',")[0]
            column_name = command.split("', '")[1].split("')")[0]
            processed_commands.append(('drop_column', table_name, column_name))
    return processed_commands
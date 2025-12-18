"""
QUESTION:
Create a function `parse_migration_commands(migration_commands)` that takes a list of migration commands as input, where each command is a string with the format `"migrations.<operation_type>(model_name='<model_name>', field_details='<field_details>'),"`. The function should return a list of dictionaries, with each dictionary containing the operation type, model name, and field details extracted from a single migration command. 

The operation type, model name, and field details should be extracted from each command and returned in the following dictionary format: `{'operation_type': '<operation_type>', 'model_name': '<model_name>', 'field_details': '<field_details>'}`.
"""

from typing import List, Dict

def entance(migration_commands: List[str]) -> List[Dict[str, str]]:
    parsed_migrations = []
    for command in migration_commands:
        parts = command.split('(')[0].split('.')
        operation_type = parts[1]
        model_name = command.split("model_name='")[1].split("',")[0]
        field_details = command.split("field_details='")[1].split("')")[0]
        parsed_migrations.append({
            'operation_type': operation_type,
            'model_name': model_name,
            'field_details': field_details
        })
    return parsed_migrations
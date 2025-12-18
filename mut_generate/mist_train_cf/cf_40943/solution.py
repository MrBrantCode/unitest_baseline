"""
QUESTION:
Create a function `generate_sql` that takes a list of migration operations as input and returns a list of SQL statements. The migration operations can be one of four types: `RenameField`, `AddField`, `RemoveField`, or `AlterField`. Each type of operation should generate a corresponding SQL statement in the following format:

- `RenameField`: `ALTER TABLE <model_name> RENAME COLUMN <old_name> TO <new_name>;`
- `AddField`: `ALTER TABLE <model_name> ADD COLUMN <field_name> <field_type>;`
- `RemoveField`: `ALTER TABLE <model_name> DROP COLUMN <field_name>;`
- `AlterField`: `ALTER TABLE <model_name> ALTER COLUMN <field_name> TYPE <new_field_type>;`

The function should return the SQL statements in the same order as the input migration operations. The function signature is `def generate_sql(migration_operations: List[Union[RenameField, AddField, RemoveField, AlterField]]) -> List[str]:`
"""

from typing import List, Union

class RenameField:
    def __init__(self, model_name, old_name, new_name):
        self.model_name = model_name
        self.old_name = old_name
        self.new_name = new_name

class AddField:
    def __init__(self, model_name, field_name, field_type):
        self.model_name = model_name
        self.field_name = field_name
        self.field_type = field_type

class RemoveField:
    def __init__(self, model_name, field_name):
        self.model_name = model_name
        self.field_name = field_name

class AlterField:
    def __init__(self, model_name, field_name, new_field_type):
        self.model_name = model_name
        self.field_name = field_name
        self.new_field_type = new_field_type

def generate_sql(migration_operations: List[Union[RenameField, AddField, RemoveField, AlterField]]) -> List[str]:
    sql_statements = []
    for operation in migration_operations:
        if isinstance(operation, RenameField):
            sql_statements.append(f'ALTER TABLE {operation.model_name} RENAME COLUMN {operation.old_name} TO {operation.new_name};')
        elif isinstance(operation, AddField):
            sql_statements.append(f'ALTER TABLE {operation.model_name} ADD COLUMN {operation.field_name} {operation.field_type};')
        elif isinstance(operation, RemoveField):
            sql_statements.append(f'ALTER TABLE {operation.model_name} DROP COLUMN {operation.field_name};')
        elif isinstance(operation, AlterField):
            sql_statements.append(f'ALTER TABLE {operation.model_name} ALTER COLUMN {operation.field_name} TYPE {operation.new_field_type};')
    return sql_statements
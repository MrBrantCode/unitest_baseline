"""
QUESTION:
Write a Python function `generate_migration_code` that takes in a list of model names and a new maximum length as input, and returns a string representing the migration code to alter the `name` field for each model to have the specified new maximum length. The `name` field is of type `CharField` and is marked as unique. The function should have the following signature:

```python
def generate_migration_code(model_names: List[str], new_max_length: int) -> str:
```
"""

from typing import List

def generate_migration_code(model_names: List[str], new_max_length: int) -> str:
    migration_code = ""
    for model_name in model_names:
        migration_code += f"migrations.AlterField(\n"
        migration_code += f"    model_name='{model_name.lower()}',\n"
        migration_code += f"    name='name',\n"
        migration_code += f"    field=models.CharField(max_length={new_max_length}, unique=True),\n"
        migration_code += f"),\n\n"
    return migration_code
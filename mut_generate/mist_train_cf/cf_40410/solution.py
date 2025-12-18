"""
QUESTION:
Create a function `apply_migrations` that takes the initial state of a database schema and a list of migration operations as input and returns the final state of the database schema after applying all the migrations.

The initial state is a dictionary where keys are model names and values are lists of fields, each field represented as a string. The migration operations are a list of objects, each with a `type` attribute and a `model_name` attribute.

Supported migration operations are:
- `AddField`: adds a new field to the specified model.
- `CreateModel`: creates a new model with the specified fields.
- `AlterField`: alters an existing field in the specified model.

The function should return the updated database schema after applying all the migrations.
"""

def apply_migrations(initial_state, operations):
    """
    Applies a list of migration operations to an initial database schema.

    Args:
    initial_state (dict): The initial state of the database schema.
    operations (list): A list of migration operations.

    Returns:
    dict: The final state of the database schema after applying all the migrations.
    """

    class MigrationOperation:
        def __init__(self, model_name):
            self.model_name = model_name

    class AddField(MigrationOperation):
        def __init__(self, model_name, field):
            super().__init__(model_name)
            self.field = field

        def apply(self, schema):
            if self.model_name in schema:
                schema[self.model_name].append(self.field)
            return schema

    class CreateModel(MigrationOperation):
        def __init__(self, model_name, fields):
            super().__init__(model_name)
            self.fields = fields

        def apply(self, schema):
            schema[self.model_name] = self.fields
            return schema

    class AlterField(MigrationOperation):
        def __init__(self, model_name, field, new_field):
            super().__init__(model_name)
            self.field = field
            self.new_field = new_field

        def apply(self, schema):
            if self.model_name in schema and self.field in schema[self.model_name]:
                index = schema[self.model_name].index(self.field)
                schema[self.model_name][index] = self.new_field
            return schema

    schema = initial_state.copy()
    for operation in operations:
        if isinstance(operation, dict):
            if operation['type'] == 'AddField':
                op = AddField(operation['model_name'], operation['field'])
            elif operation['type'] == 'CreateModel':
                op = CreateModel(operation['model_name'], operation['fields'])
            elif operation['type'] == 'AlterField':
                op = AlterField(operation['model_name'], operation['field'], operation['new_field'])
            schema = op.apply(schema)
        else:
            schema = operation.apply(schema)
    return schema
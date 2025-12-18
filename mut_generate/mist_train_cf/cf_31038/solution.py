"""
QUESTION:
Create a `Field` class that represents a field in a data model. Implement a `make_field` function that takes two parameters, `name` (string) and `type` (string), and returns an instance of the `Field` class with the specified name and type. The `Field` class should have properties `name` and `type` and two read-only properties: `mock_value` and `mock_value_original_type`. If the `type` is 'TYPE_BYTES', `mock_value` and `mock_value_original_type` should return the name followed by "_blob" as bytes (e.g., `b'foo_bar_blob'` for the name 'foo_bar').
"""

class Field:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    @property
    def mock_value(self):
        if self.type == 'TYPE_BYTES':
            return bytes(f"{self.name}_blob", 'utf-8')

    @property
    def mock_value_original_type(self):
        if self.type == 'TYPE_BYTES':
            return f"{self.name}_blob".encode('utf-8')


def make_field(name, type):
    return Field(name, type)
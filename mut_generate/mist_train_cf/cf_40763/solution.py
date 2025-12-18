"""
QUESTION:
Implement the function `format_import_statements(import_statements)` that takes a list of `ImportStatement` objects and returns a string with each import statement and its associated import parts formatted in a readable way. Each `ImportStatement` object has a `module_name` and a list of `ImportAsPart` objects, each representing an import part with `module_name`, `alias`, and optional `comment`. The function should return a string with the module name followed by its import parts, formatted as shown in the example.
"""

def format_import_statements(import_statements):
    formatted_output = ""
    for statement in import_statements:
        formatted_output += f"{statement.module_name}\n"
        for part in statement.import_parts:
            if part.alias:
                formatted_output += f"    {part.module_name} as {part.alias}\n"
            else:
                formatted_output += f"    {part.module_name}"
                if part.comment:
                    formatted_output += f"  # {part.comment}"
                formatted_output += "\n"
    return formatted_output
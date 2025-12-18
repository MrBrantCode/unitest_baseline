"""
QUESTION:
Create a function named `process_imports` that takes a list of strings representing Python import statements as input. The function should return a dictionary where the keys are the module names and the values are the corresponding import statements. The function should handle both direct imports (e.g., "import os") and relative imports (e.g., "from .DPYClient import DPYClient"), but ignore any non-import statements (e.g., "except ModuleNotFoundError"). The module name for relative imports should be the name of the imported module, not the package.
"""

def process_imports(import_list: list) -> dict:
    import_dict = {}
    for import_statement in import_list:
        if "import " in import_statement:
            module_name = import_statement.split("import ")[1].split()[0]
            import_dict[module_name] = import_statement
        elif "from " in import_statement:
            module_name = import_statement.split("import ")[1].split()[0]
            import_dict[import_statement.split("import ")[1].split()[0]] = import_statement
    return import_dict
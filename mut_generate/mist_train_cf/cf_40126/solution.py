"""
QUESTION:
Design a function or class method, `build_source_location_table`, that takes in a list of source paths and their corresponding text content. The function should handle imports in the form `(import "path/to/module")`, detect circular dependencies, and build a source location table. The source location table should be a dictionary where the keys are the source paths and the values are the lengths of the corresponding source code. The function should also detect and report errors in the imported code.
"""

def build_source_location_table(sources):
    """
    Builds a source location table from the given list of source paths and their corresponding text content.
    
    Args:
    sources (list): A list of tuples containing the source paths and their corresponding text content.
    
    Returns:
    dict: A dictionary where the keys are the source paths and the values are the lengths of the corresponding source code.
    """
    source_location_table = {}
    source_code_dict = {}

    for path, text in sources:
        source_code_dict[path] = text

    def process_imports(path, visited):
        if path in visited:
            raise Exception("Circular dependency detected")

        visited.add(path)
        lines = source_code_dict[path].split('\n')
        for line in lines:
            if line.startswith('(import "'):
                import_path = line.split('"')[1]
                if import_path not in source_code_dict:
                    raise Exception(f"Error: Imported module '{import_path}' not found")
                process_imports(import_path, visited)
        visited.remove(path)

    for path, text in source_code_dict.items():
        try:
            process_imports(path, set())
            source_location_table[path] = len(text)
        except Exception as e:
            print(f"Error processing {path}: {str(e)}")

    return source_location_table
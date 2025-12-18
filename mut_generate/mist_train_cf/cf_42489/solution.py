"""
QUESTION:
Implement the `generate_documentation` function that takes a Python module name as input and generates documentation for it. The function should perform the following steps:
1. Import the specified module dynamically.
2. Extract information about the module's classes, functions, and their docstrings.
3. Format this information into a human-readable document.

The function should be able to handle various types of modules with different classes and functions, and it should generate the documentation in a clear and organized manner. It should also handle the following cases:
- The module contains classes with methods and docstrings.
- The module contains standalone functions with docstrings.
- The module contains nested classes and functions with docstrings.
"""

import importlib
import inspect

def generate_documentation(module_name):
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Error: Module '{module_name}' not found.")
        return

    print(f"Documentation for {module_name}:\n")

    # Module docstring
    print(f"Module docstring:\n{inspect.getdoc(module)}\n")

    # Classes and their methods
    classes = inspect.getmembers(module, inspect.isclass)
    for class_name, class_obj in classes:
        print(f"Class: {class_name}")
        print(f"    - {inspect.getdoc(class_obj)}")
        methods = inspect.getmembers(class_obj, inspect.isfunction)
        if methods:
            print("    - Methods:")
            for method_name, method_obj in methods:
                print(f"        - {method_name}")
                print(f"            - {inspect.getdoc(method_obj)}")
        print()

    # Standalone functions
    functions = inspect.getmembers(module, inspect.isfunction)
    if functions:
        print("Functions:")
        for function_name, function_obj in functions:
            if function_name != '<lambda>':
                print(f"1. {function_name}")
                print(f"    - {inspect.getdoc(function_obj)}")
        print()
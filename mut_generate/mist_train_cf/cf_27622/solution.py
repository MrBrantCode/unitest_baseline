"""
QUESTION:
Write a function called `parse_setup_file` that takes a string representing the contents of a setup.py file as input and returns a dictionary containing the Python version required, installation dependencies, test dependencies, and development status classifiers. The dictionary should have the keys 'python_requires', 'install_requires', 'tests_require', and 'classifiers'. The function should be able to handle a setup.py file with the format of assignment statements (e.g., `variable_name='value'`) and list assignments (e.g., `variable_name=['value1', 'value2']`). If the setup.py file has an invalid format, the function should catch the SyntaxError and handle it accordingly. The function should return an empty dictionary if the setup.py file is invalid.
"""

import ast

def parse_setup_file(setup_content: str) -> dict:
    setup_dict = {}
    try:
        setup_ast = ast.parse(setup_content)
        for node in setup_ast.body:
            if isinstance(node, ast.Assign):
                if isinstance(node.value, ast.List):
                    value = [ast.literal_eval(v) for v in node.value.elts]
                elif isinstance(node.value, ast.Str):
                    value = node.value.s
                else:
                    continue
                if node.targets[0].id == 'python_requires':
                    setup_dict['python_requires'] = value
                elif node.targets[0].id == 'install_requires':
                    setup_dict['install_requires'] = value
                elif node.targets[0].id == 'tests_require':
                    setup_dict['tests_require'] = value
                elif node.targets[0].id == 'classifiers':
                    setup_dict['classifiers'] = value
    except SyntaxError:
        print("Invalid setup.py file format")
    return setup_dict
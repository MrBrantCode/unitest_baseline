"""
QUESTION:
Create a Python function `execute_module_function` that takes two parameters: 
- `module_name` (string): The name of the module to be imported and executed.
- `function_name` (string): The name of the function to be executed within the imported module.

This function should dynamically import the specified module, execute the specified function within that module, and return the result of the function execution. Assume the specified module and function exist and are accessible from the current working directory.
"""

def execute_module_function(module_name, function_name):
    import importlib

    try:
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)
        result = function()
        return result
    except ModuleNotFoundError:
        return f"Module '{module_name}' not found."
    except AttributeError:
        return f"Function '{function_name}' not found in module '{module_name}'."
    except Exception as e:
        return f"An error occurred while executing the function: {e}"
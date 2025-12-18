"""
QUESTION:
Implement a Python function `generate_simulation_summary(expressions, methods, parameters, functions)` that takes four dictionaries as input: 
- `expressions`: A dictionary containing expressions as keys and their corresponding values.
- `methods`: A dictionary containing simulation methods as keys and their corresponding values.
- `parameters`: A dictionary containing parameter names as keys and their corresponding sub-dictionaries with parameter values.
- `functions`: A dictionary containing function names as keys and their corresponding values.

Return a formatted string that summarizes the simulation setup. The output string should have the following structure:
- Expressions, methods, parameters, and functions should be listed in this order.
- Each section should be separated by a newline character.
- Expressions, methods, and functions should be listed as key-value pairs, one pair per line, with a hyphen and a space before each key.
- Parameters should be listed with their sub-parameters indented under them, also as key-value pairs, one pair per line.
- Indentation should be used consistently throughout the summary.
"""

def generate_simulation_summary(expressions, methods, parameters, functions):
    summary = "Simulation Summary:\n"
    
    # Process and append expressions
    summary += "Expressions:\n"
    for exp, val in expressions.items():
        summary += f"- {exp}: {val}\n"
    
    # Process and append methods
    summary += "\nMethods:\n"
    for method, val in methods.items():
        summary += f"- {method}: {val}\n"
    
    # Process and append parameters
    summary += "\nParameters:\n"
    for param, sub_params in parameters.items():
        summary += f"- {param}:\n"
        for sub_param, val in sub_params.items():
            summary += f"  - {sub_param}: {val}\n"
    
    # Process and append functions
    summary += "\nFunctions:\n"
    for func, val in functions.items():
        summary += f"- {func}: {val}\n"
    
    return summary
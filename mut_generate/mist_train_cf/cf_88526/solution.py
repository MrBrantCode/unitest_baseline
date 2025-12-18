"""
QUESTION:
Create a class named `CustomDataStructure` with the following properties and methods:

- Store variables in a data structure.
- Support addition, subtraction, multiplication, and division operations between the variables stored in it. 
- The time complexity of each operation should be less than O(log n), where n is the number of variables stored in the data structure.
- The space complexity of the data structure should be less than O(n).
- Support the following additional methods:
  - `get_variables()`: Return a list of all variables currently stored in the data structure.
  - `delete_variable(variable_name)`: Remove the variable with the specified name from the data structure.
  - `update_variable(variable_name, new_value)`: Update the value of the variable with the specified name to the new value.
  - `add_variable(variable_name, value)`: Add a new variable to the data structure.
  - `add(variable1, variable2)`, `subtract(variable1, variable2)`, `multiply(variable1, variable2)`, `divide(variable1, variable2)`: Perform mathematical operations on variables.
"""

def entrance(variables, operation, variable1, variable2=None, new_value=None):
    variables = variables
    
    def add_variable(variable_name, value):
        variables[variable_name] = value

    def get_variables():
        return list(variables.keys())

    def delete_variable(variable_name):
        del variables[variable_name]

    def update_variable(variable_name, new_value):
        variables[variable_name] = new_value

    def add(var1, var2):
        return variables[var1] + variables[var2]

    def subtract(var1, var2):
        return variables[var1] - variables[var2]

    def multiply(var1, var2):
        return variables[var1] * variables[var2]

    def divide(var1, var2):
        return variables[var1] / variables[var2]

    if operation == "add_variable":
        add_variable(variable1, variable2)
    elif operation == "get_variables":
        return get_variables()
    elif operation == "delete_variable":
        delete_variable(variable1)
    elif operation == "update_variable":
        update_variable(variable1, variable2)
    elif operation == "add":
        return add(variable1, variable2)
    elif operation == "subtract":
        return subtract(variable1, variable2)
    elif operation == "multiply":
        return multiply(variable1, variable2)
    elif operation == "divide":
        return divide(variable1, variable2)
    else:
        return "Invalid operation"

    return variables
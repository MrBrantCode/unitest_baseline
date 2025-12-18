"""
QUESTION:
Write a function named `check_variable` that takes one argument. The function should identify the data type of the argument, check if it's a float, and attempt to convert it to a float if it's not. If the conversion fails, it should print an error message. If the argument or converted value is a float, the function should check if it falls within the range of 0.01 to 50.0 and print a message accordingly. The function should handle errors and exceptions to prevent breaking during execution.
"""

def check_variable(var):
    var_type = type(var)

    if var_type != float:
        print(f"The type of the variable is: {var_type}")
        try:
            var = float(var)
            print("Variable has been converted to float.")
        except:
            print("Error: Variable could not be converted to float.")
            return
    else:
        print("The type of the variable is: float.")

    if 0.01 <= var <= 50.0:
        print(f"The variable is a legitimate distance measurement: {var} miles")
    else:
        print(f"Error: The variable is not a legitimate distance measurement: {var} miles")
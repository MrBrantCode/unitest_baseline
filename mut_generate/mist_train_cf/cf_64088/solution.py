"""
QUESTION:
Write a function named `function_sum` that takes two parameters, checks if they are numbers, and then calculates and prints their sum. The function should handle potential data type errors and provide informative error messages. Ensure the function is context-independent and can be used with various input sources, such as user input or variables.
"""

def function_sum(param1, param2):
    try:
        param1 = float(param1)
        param2 = float(param2)
    except ValueError:
        print("Invalid input. Enter numbers only.")
        return
    
    result = param1 + param2
    print('Sum of parameters: ' + str(result))
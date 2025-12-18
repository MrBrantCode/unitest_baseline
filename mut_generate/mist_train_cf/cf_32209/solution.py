"""
QUESTION:
Write a function called `is_valid_return_statement` that takes a string `input_string` as input and returns a boolean indicating whether the string is a valid return statement according to the given grammar rules. A return statement consists of the keyword "return" followed by either a semicolon or an expression followed by a semicolon. The function should only consider the syntax of the input string and not the semantics of the expressions, and should ignore any leading or trailing whitespace in the input string.
"""

def entrance(input_string: str) -> bool:
    input_string = input_string.strip()  
    if input_string.startswith("return "):  
        input_string = input_string[len("return "):]  
        if input_string.endswith(";"):  
            input_string = input_string[:-1]  
            return input_string == "" or not input_string.isspace()  
    return False  
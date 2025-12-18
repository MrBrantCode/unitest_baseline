"""
QUESTION:
Create a function `process_input` that takes a string `input_str` as input and returns a dictionary. 

The function should determine the type of the input string and add a corresponding key-value pair to the result dictionary: "integer" if the string is a valid integer, "float" if the string is a valid float, and "string" otherwise. 

If the input string is empty, return a dictionary with "code" set to 400 and "msg" set to "Empty input string". If an exception occurs during processing, return a dictionary with "code" set to 401 and "msg" set to the string representation of the exception.
"""

def process_input(input_str):
    result = {}
    try:
        if input_str == "":
            result["code"] = 400
            result["msg"] = "Empty input string"
        elif input_str.isdigit():
            result["input_type"] = "integer"
        elif input_str.replace('.', '', 1).isdigit():
            result["input_type"] = "float"
        else:
            result["input_type"] = "string"
    except Exception as e:
        result["code"] = 401
        result["msg"] = str(e)
    return result
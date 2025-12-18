"""
QUESTION:
Construct a function called `getName` that takes a string input and returns either "Nick" or "Jack" based on the input value. The input must contain only letters and can be a mix of uppercase and lowercase. If the input contains any non-letter characters, raise an exception. The function should have at least five cases. The output should be a string enclosed in double quotes.
"""

def getName(input):
    input = input.lower()
    
    if not input.isalpha():
        raise Exception("Invalid input")
    
    switch = {
        "nick": "Nick",
        "jack": "Jack",
        "alex": "Jack",
        "sam": "Nick",
        "mike": "Jack"
    }
    
    return switch.get(input, "Invalid input")
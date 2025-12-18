"""
QUESTION:
Create a function named `getName` that takes a non-empty string as input and returns either "Nick" or "Jack" based on the input value. The function should handle inputs containing uppercase letters by converting them to lowercase, but throw an exception for inputs containing special characters or numbers. The function should have at least five distinct input values mapped to "Nick" or "Jack".
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
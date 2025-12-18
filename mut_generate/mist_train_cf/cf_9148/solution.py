"""
QUESTION:
Write a function named `snake_to_camel` that takes a string in snake_case as input and returns the string converted to camelCase. The input string will only contain lowercase alphabets and underscores, will not be empty, will not start with an underscore, and may contain multiple consecutive underscores which should be treated as a single underscore in the final camelCase output.
"""

def entrance(snake_case):
    words = snake_case.split('_')
    camel_case = words[0]
    
    for word in words[1:]:
        camel_case += word.capitalize()
        
    return camel_case
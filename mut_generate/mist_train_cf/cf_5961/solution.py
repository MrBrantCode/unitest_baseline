"""
QUESTION:
Write a function `snake_case_to_camel_case` that takes a string in snake_case format as input, converts it to CamelCase, and returns the result. The function should handle empty strings, strings containing numbers or special characters, and should have a time complexity of O(n) and space complexity of O(1). If the input string contains numbers or special characters after the first character of each word, raise an exception.
"""

def snake_case_to_camel_case(snake_case_string):
    if snake_case_string == "":
        return ""
    
    words = snake_case_string.split("_")
    camel_case_string = ""
    
    for word in words:
        if word == "":
            continue
            
        if word[0].isdigit() or not word[0].isalpha():
            word = word[1:]
            
        if word == "":
            continue
            
        word = word.capitalize()
        
        if any(char.isdigit() or not char.isalpha() for char in word):
            raise Exception("Invalid string")
        
        camel_case_string += word
        
    return camel_case_string
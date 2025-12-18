"""
QUESTION:
Implement a function `process_data_entries(data)` that takes a list of tuples, where each tuple contains a code and a name, and returns a dictionary where the code serves as the key and the name as the value. If a code appears multiple times in the input list, append a unique identifier to the code to make it unique before using it as a key in the dictionary. The unique identifier should be a number starting from 1 and incremented for each duplicate code.
"""

def process_data_entries(data):
    code_count = {}
    result = {}
    
    for code, name in data:
        if code in code_count:
            code_count[code] += 1
        else:
            code_count[code] = 1
        
        if code_count[code] > 1:
            key = f"{code}_{code_count[code]}"
        else:
            key = code
        
        result[key] = name
    
    return result
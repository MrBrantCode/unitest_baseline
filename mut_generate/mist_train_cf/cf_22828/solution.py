"""
QUESTION:
Create a function named `classify_code` that takes a string of Python code as input and returns one of the following classifications: "single statement", "multiple statement", or "control flow statement". The function should analyze the structure of the input code and classify it accordingly. The classification rules are as follows: 

- If the code contains a semicolon (;), it's classified as a "multiple statement".
- If the code contains any control flow keywords ("if", "else", "elif", "for", "while", "switch", "case"), it's classified as a "control flow statement".
- If the code doesn't match the above conditions, it's classified as a "single statement".
"""

def classify_code(code):
    # Remove whitespace and newlines from the code snippet
    code = code.replace(" ", "").replace("\n", "")
    
    # Check if the code snippet contains multiple statements
    if ';' in code:
        return "multiple statement"
    
    # Check if the code snippet contains a control flow statement
    control_flow_keywords = ["if", "else", "elif", "for", "while", "switch", "case"]
    for keyword in control_flow_keywords:
        if keyword in code:
            return "control flow statement"
    
    # If none of the above conditions are met, classify as a single statement
    return "single statement"
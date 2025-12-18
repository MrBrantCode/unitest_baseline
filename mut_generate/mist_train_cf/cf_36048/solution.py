"""
QUESTION:
Create a function `analyze_flow_control` that takes a code snippet as input, identifies the flow control structures used (if statements, for loops, while loops), and returns a dictionary containing the frequency of each type of flow control structure. The function should only count exact matches for "if ", "for ", and "while ".
"""

def analyze_flow_control(code_snippet):
    flow_control_counts = {
        "if": code_snippet.count("if "),
        "for": code_snippet.count("for "),
        "while": code_snippet.count("while ")
    }
    return flow_control_counts
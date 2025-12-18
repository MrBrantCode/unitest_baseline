"""
QUESTION:
Implement the function `prepare_data` that takes a list of strings `lines` as input, processes each line to exactly 20 characters by padding or truncating it, accumulates the processed lines into a single string, and returns the accumulated data as a string of exactly 80 characters by padding or truncating it. The function should not include any delay or control signals.
"""

def prepare_data(lines):
    data = ""
    for ln in lines:
        line = ln + "                    "  
        data += line[0:20]  
    if len(data) < 80:
        data += " " * (80 - len(data))  
    return data[0:80]
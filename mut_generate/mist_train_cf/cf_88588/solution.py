"""
QUESTION:
Write a function `clear_line_breaks` that takes two parameters: `input_string` and `ignore_char`. It should return a string with line breaks removed, leading/trailing white spaces removed from each line, and lines starting with `ignore_char` ignored. The function should handle special characters and symbols in the input string.
"""

def clear_line_breaks(input_string, ignore_char):
    lines = input_string.split("\n")  # Split the input string into lines
    
    # Iterate through each line, apply filters, and remove line breaks
    cleaned_lines = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing white spaces
        
        # Ignore lines starting with the specified character
        if not line.startswith(ignore_char):
            cleaned_lines.append(line)
    
    cleaned_string = "\n".join(cleaned_lines)  # Join the cleaned lines back into a string
    return cleaned_string
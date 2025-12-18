"""
QUESTION:
Create a function called `convert_to_html_entities` that takes a string as input and returns a new string where all characters with ASCII values less than 128 are replaced with their corresponding HTML entities. Use the following mapping for HTML entities: 34 to &quot;, 38 to &amp;, 60 to &lt;, and 62 to &gt;. The input string should have a maximum length of 1000 characters, and the output string should have a maximum length of 2000 characters. If the length of the result string exceeds 2000 characters during processing, stop converting characters and return the resulting string truncated to 2000 characters.
"""

def convert_to_html_entities(string):
    html_entities = {
        34: "&quot;",
        38: "&amp;",
        60: "&lt;",
        62: "&gt;"
    }
    
    result = ""
    for char in string:
        ascii_value = ord(char)
        if ascii_value < 128:
            html_entity = html_entities.get(ascii_value, char)
            result += html_entity
        else:
            result += char
        
        if len(result) >= 2000:
            break
    
    return result[:2000]
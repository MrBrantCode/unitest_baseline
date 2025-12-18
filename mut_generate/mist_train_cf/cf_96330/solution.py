"""
QUESTION:
Write a function `convert_to_html_entities` that takes a string as input, replaces characters with their corresponding HTML entities if the ASCII value is less than 128, and returns the resulting string. The function should use the following HTML entities: &quot; for ASCII value 34, &amp; for ASCII value 38, &lt; for ASCII value 60, and &gt; for ASCII value 62. If the ASCII value is not found, the character should be left unchanged. The input string can have a maximum length of 1000 characters, and the output string should have a maximum length of 2000 characters.
"""

def convert_to_html_entities(s):
    html_entities = {
        34: "&quot;",
        38: "&amp;",
        60: "&lt;",
        62: "&gt;"
    }
    
    result = ""
    for char in s:
        ascii_value = ord(char)
        if ascii_value < 128:
            html_entity = html_entities.get(ascii_value, char)
            result += html_entity
        else:
            result += char
        
        if len(result) >= 2000:
            break
    
    return result[:2000]
"""
QUESTION:
Create a function called replace_html_entities that takes a string as input. The function should replace the characters in the string with their corresponding HTML entities based on the ASCII values of the characters. If the ASCII value of a character is less than 128 and corresponds to a special HTML entity (&quot;, &amp;, &lt;, or &gt;), replace the character with its corresponding entity; otherwise, leave the character unchanged. The function should return the resulting string with the replaced HTML entities.
"""

def replace_html_entities(string):
    result = ""
    for char in string:
        if ord(char) == 34:
            result += "&quot;"
        elif ord(char) == 38:
            result += "&amp;"
        elif ord(char) == 60:
            result += "&lt;"
        elif ord(char) == 62:
            result += "&gt;"
        else:
            result += char
    return result
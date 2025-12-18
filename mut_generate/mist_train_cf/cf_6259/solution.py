"""
QUESTION:
Create a function `replace_html_entities(string)` that takes a string of up to 1000 characters as input and returns the string with certain characters replaced with their corresponding HTML entities based on their ASCII values. The replacement rules are as follows: ASCII value 34 is replaced with &quot;, 38 with &amp;, 60 with &lt;, and 62 with &gt;. The output string should be truncated to a maximum length of 2000 characters. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def replace_html_entities(string):
    html_entities = {
        34: '&quot;',
        38: '&amp;',
        60: '&lt;',
        62: '&gt;'
    }
    result = ""
    for char in string:
        ascii_value = ord(char)
        if ascii_value in html_entities:
            result += html_entities[ascii_value]
        else:
            result += char
    return result[:2000]
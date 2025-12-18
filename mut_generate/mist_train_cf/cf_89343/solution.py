"""
QUESTION:
Write a function `replace_html_entities(string)` that takes a string as input and replaces certain characters with their corresponding HTML entities based on their ASCII values. The function should map the following ASCII values to their corresponding HTML entities: 34 to &quot;, 38 to &amp;, 60 to &lt;, and 62 to &gt;. The input string can have a maximum length of 1000 characters, and the output string should have a maximum length of 2000 characters. The function should have a time complexity of O(n), where n is the length of the input string.
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
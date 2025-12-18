"""
QUESTION:
Implement a function `escape_string` that takes a string as input and returns the escaped string. In the returned string, backslashes should be escaped as double backslashes, and other characters with Unicode numerical value greater than 127 or special characters should be replaced with their corresponding escape sequences: ``'\\xYY'``, ``'\\uYYYY'``, or ``'\\UYYYYYYYY'``, where Y represents hex digits depending on the Unicode numerical value of the character. The function should handle various input cases.
"""

def escape_string(pth: str) -> str:
    escaped = ""
    for char in pth:
        if char == '\\':
            escaped += '\\\\'  # Escape backslashes as double backslashes
        elif char in ['\n', '\t', '\r', '\b', '\f']:
            # Replace special characters with their corresponding escape sequences
            escaped += '\\' + format(ord(char), 'x').zfill(2)  # Using '\\xYY' format
        else:
            if ord(char) > 127:
                if ord(char) < 0x10000:
                    escaped += '\\u' + format(ord(char), 'x').zfill(4)  # Using '\\uYYYY' format for Unicode characters
                else:
                    escaped += '\\U' + format(ord(char), 'x').zfill(8)  # Using '\\UYYYYYYYY' format for Unicode characters
            else:
                escaped += char
    return escaped
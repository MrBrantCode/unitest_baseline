"""
QUESTION:
Create a function `format_output` that formats a string with stderr, ensuring the resulting string does not exceed a specified maximum length. The function should take two parameters: `stderr` (1 <= |stderr| <= 1000), a string containing characters captured from stderr, and `max_len` (1 <= max_len <= 1000), an integer representing the maximum length of the formatted string to be returned.

The formatted string should contain stderr and if its length exceeds `max_len`, it should be truncated to fit within the specified length, with the truncated string ending in "..." to indicate truncation.
"""

def format_output(stderr: str, max_len: int) -> str:
    if len(stderr) <= max_len:
        return stderr
    else:
        return stderr[:max_len-3] + "..."
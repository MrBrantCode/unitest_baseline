"""
QUESTION:
Write a function named `decode_string` that takes a string `s` as input, replaces special characters (`&amp;`, `&lt;`, `&gt;`, `&quot;`, and `&#39;`) with their original forms (`&`, `<`, `>`, `"`, and `'`), and returns the decoded string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string manipulation methods or regular expressions.
"""

def decode_string(s):
    decoded_string = ""
    special_chars = {
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&quot;": "\"",
        "&#39;": "'"
    }
    
    i = 0
    while i < len(s):
        if s[i] == "&":
            end_index = s.find(";", i)
            if end_index != -1:
                substr = s[i:end_index + 1]
                if substr in special_chars:
                    decoded_string += special_chars[substr]
                    i = end_index + 1
                    continue
        decoded_string += s[i]
        i += 1
    
    return decoded_string
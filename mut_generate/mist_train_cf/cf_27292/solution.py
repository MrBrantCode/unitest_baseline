"""
QUESTION:
Write a function `extract_decrypted_messages` that takes a string `code_snippet` as input. The string contains a series of characters and placeholder text denoted by `<KEY>`. The function should return a list of strings where each string is a line from the input that does not contain `<KEY>` and is not empty.
"""

def extract_decrypted_messages(code_snippet):
    decrypted_messages = []
    lines = code_snippet.split('\n')
    for line in lines:
        if line and '<KEY>' not in line:
            decrypted_messages.append(line)
    return decrypted_messages
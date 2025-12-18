"""
QUESTION:
Write a function `decode_message(encoded_message: str) -> str` that takes an encoded message as input and returns the decoded message. The encoded message is a string containing various marks where only one mark is different from the rest. The decoded message is obtained by moving not more than two characters forward and not more than three characters backward from the position of the unique mark. If no unique mark is found, return "No unique mark found in the encoded message".
"""

def decode_message(encoded_message: str) -> str:
    unique_mark = None
    for char in encoded_message:
        if encoded_message.count(char) == 1:
            unique_mark = char
            break

    if unique_mark is None:
        return "No unique mark found in the encoded message"

    unique_mark_index = encoded_message.index(unique_mark)
    forward_index = min(unique_mark_index + 2, len(encoded_message) - 1)
    backward_index = max(unique_mark_index - 3, 0)

    return encoded_message[backward_index:forward_index+1]
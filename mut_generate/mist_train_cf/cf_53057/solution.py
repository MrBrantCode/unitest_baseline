"""
QUESTION:
Implement a function `double_cipher(text)` that takes an input string and returns the encrypted string by applying a substitution cipher followed by a transposition cipher. The substitution cipher should replace each lowercase alphabet character with the next alphabet character in a cyclic manner (i.e., 'z' becomes 'a'), and the transposition cipher should rearrange the characters based on a column-based transposition with a column number equal to the square root of the length of the input string. Do not use any external libraries for the transposition cipher. The function should have a time complexity of O(n) and space complexity of O(n), where n is the length of the input string.
"""

def double_cipher(text):
    cipher = {k:chr((ord(k) - 97 + 1) % 26 + 97) for k in map(chr, range(97, 123))}
    message_len = len(text)
    column_num = int(message_len ** 0.5)
    substituted_text = ''.join(cipher[c] if c in cipher else c for c in text)
    encrypted_text = ''

    for column_idx in range(column_num):
        pointer = column_idx
        while pointer < message_len:
            encrypted_text += substituted_text[pointer]
            pointer += column_num

    return encrypted_text
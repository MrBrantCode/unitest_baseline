"""
QUESTION:
Create two functions, `replace_chars` and `create_unique_hash`. The `replace_chars` function should take an input string and a hash table as inputs, and return the string with all characters replaced according to the hash table. The `create_unique_hash` function should take an input string and return a hash table where each character in the string is mapped to a unique non-ASCII character. The functions should be able to handle large strings efficiently and support any kind of input, including special characters and emojis.
"""

def replace_chars(input_string, hash_table):
    output_string = ""
    for char in input_string:
        if char in hash_table:
            output_string += hash_table[char]
        else:
            output_string += char
    return output_string


def create_unique_hash(input_string):
    hash_table = {}
    for char in input_string:
        hash_table[char] = chr(ord(char) + 1000)  # adding 1000 to ASCII value to make it non-ASCII
    return hash_table
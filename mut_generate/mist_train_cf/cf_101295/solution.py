"""
QUESTION:
Create a function called `to_chinese` that takes a string of Unicode code points as input and returns its corresponding Chinese characters. The function should map each Unicode code point to its corresponding Chinese character using a lookup table, and then concatenate the Chinese characters together to form the final string. The function should be able to handle a list of Unicode code points and return an empty string if a code point is not found in the lookup table.
"""

# Define a lookup table mapping Unicode code points to Chinese characters
lookup = {
    19968: '一',
    19969: '丁',
    19970: '丂',
    # add more mappings here...
}

# Define a function to convert a string into its corresponding Chinese characters using Unicode
def to_chinese(text):
    # Convert the string into a list of Unicode code points
    code_points = [ord(c) for c in text]
    
    # Map each Unicode code point to its corresponding Chinese character using the lookup table
    chinese_chars = [lookup.get(cp, '') for cp in code_points]
    
    # Concatenate the Chinese characters together to form the final string
    return ''.join(chinese_chars)
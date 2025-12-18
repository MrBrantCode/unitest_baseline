"""
QUESTION:
Implement a function `compress_string(input_str)` to compress a given string using a run-length encoding algorithm. The function should take a string as input, replace all occurrences of ' a ' with ' the ', and then compress the string by replacing sequences of repeated characters with the count of repetitions followed by the character. Additionally, implement a corresponding function `decompress_string(input_str)` to decompress the compressed string back to its original form after the article replacement.
"""

def compress_string(input_str):
    """
    This function compresses a given string using a run-length encoding algorithm.
    
    Args:
    input_str (str): The input string to be compressed.
    
    Returns:
    str: The compressed string.
    """
    input_str = input_str.replace(' a ', ' the ')
    output_str = ""
    i = 0
    while (i <= len(input_str)-1):
        count = 1
        ch = input_str[i]
        j = i
        while (j < len(input_str)-1):
            if (input_str[j] == input_str[j+1]):
                j = j + 1
                count = count + 1
            else:
                break
        output_str = output_str + str(count) + ch
        i = j+1
    return output_str


def decompress_string(input_str):
    """
    This function decompresses a given compressed string.
    
    Args:
    input_str (str): The input string to be decompressed.
    
    Returns:
    str: The decompressed string.
    """
    output_str = ""
    count = 0
    for i in range(len(input_str)):
        if (input_str[i].isdigit()):
            count = count * 10 + int(input_str[i])
        else:
            output_str = output_str + input_str[i]*count
            count = 0
    return output_str
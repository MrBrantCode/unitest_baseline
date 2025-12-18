"""
QUESTION:
Create a function `WordCount()` that returns the word count of the current buffer as quickly as possible. The function will be executed frequently, so it must be optimized for performance. The buffer may contain thousands of lines, and the function should be able to handle this without causing significant slowdown.
"""

def word_count(buffer):
    """
    Returns the word count of the given buffer.

    This function is optimized for performance and can handle thousands of lines.

    :param buffer: The input buffer as a string
    :return: The word count of the buffer
    """
    return len(buffer.split())
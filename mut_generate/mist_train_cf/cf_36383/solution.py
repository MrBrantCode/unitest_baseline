"""
QUESTION:
Create a function `process_lines` that takes a multi-line string as input and returns a list of dictionaries. The function should split the input string into lines, and for each line, it should count the number of words, determine the longest word, and capitalize the first letter of each word. Each dictionary in the output list should contain the following keys: 'line', 'word_count', 'longest_word', and 'capitalized_line'. Assume the input string does not contain punctuation marks.
"""

def process_lines(input_str):
    result = []
    for line in input_str.splitlines():
        words = line.split()
        word_count = len(words)
        longest_word = max(words, key=len)
        capitalized_line = ' '.join(word.capitalize() for word in words)
        result.append({
            'line': line,
            'word_count': word_count,
            'longest_word': longest_word,
            'capitalized_line': capitalized_line
        })
    return result
"""
QUESTION:
Write a function `replace_the` that takes a text document as input, scans each line to replace every fifth occurrence of the word 'the' (case-insensitive) with an asterisk symbol in each line separately, and returns the transformed text. The function should reset the count for each new line and maintain the original line breaks.
"""

def replace_the(text):
    text = text.lower().split('\n')
    for i in range(len(text)):
        word_count = 0
        line = text[i].split(' ')
        for j in range(len(line)):
            if line[j] == 'the':
                word_count += 1
                if word_count == 5:
                    line[j] = '*'
                    word_count = 0
        text[i] = " ".join(line)
    return "\n".join(text)
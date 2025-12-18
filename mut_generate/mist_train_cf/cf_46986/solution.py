"""
QUESTION:
Write a function `white_space_remover` that takes a list of sentences as input. The function should return a list of sentences with no extra white spaces, maintaining the original sequence and ignoring special characters. The function should not use any built-in string manipulation functions and instead use data structures and programming logic.
"""

def white_space_remover(sentences):
    result = []
    for sentence in sentences:
        char_list = list(sentence)
        no_space = []
        space_found = False
        for char in char_list:
            if not (char.isalpha() or char.isdigit()):
                if char == ' ':
                    if not space_found:
                        no_space.append(char)
                        space_found = True
                else:
                    no_space.append(char)
            else:
                no_space.append(char)
                space_found = False
        result.append(''.join(no_space).strip())
    return result
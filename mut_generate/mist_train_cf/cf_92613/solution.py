"""
QUESTION:
Given a sentence encoded with a Caesar cipher with a shift value between 1 and 25, write a function to find the index of the string "the" in the decoded sentence. The function, named `find_index_of_the`, should return the index of "the" if found, or -1 otherwise.
"""

def find_index_of_the(sentence):
    """
    Finds the index of the string "the" in the decoded sentence.
    
    Args:
    sentence (str): The encoded sentence.
    
    Returns:
    int: The index of "the" if found, or -1 otherwise.
    """
    def caesar_decode(sentence, shift):
        decoded_sentence = ""
        for char in sentence:
            if char.isalpha():
                char_code = ord(char.lower()) - shift
                if char_code < ord('a'):
                    char_code += 26
                decoded_sentence += chr(char_code)
            else:
                decoded_sentence += char
        return decoded_sentence

    index = -1
    for shift in range(1, 26):
        decoded_sentence = caesar_decode(sentence, shift)
        if "the" in decoded_sentence.lower():
            index = decoded_sentence.lower().index("the")
            break
    return index
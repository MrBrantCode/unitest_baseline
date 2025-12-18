"""
QUESTION:
Implement the function `reveal_hidden_sentence(sentence)` that takes a string of lowercase English letters as input, where each letter is shifted by a certain number of positions in the alphabet based on its 1-indexed position in the sentence, and returns the decoded sentence. If the shift extends beyond 'z', it should wrap around to the beginning of the alphabet.
"""

def reveal_hidden_sentence(sentence: str) -> str:
    decoded_sentence = ""
    for i in range(len(sentence)):
        shift = i + 1
        char_code = ord(sentence[i]) - shift
        if char_code < ord('a'):
            char_code += 26  # Wrap around to the beginning of the alphabet
        decoded_sentence += chr(char_code)
    return decoded_sentence
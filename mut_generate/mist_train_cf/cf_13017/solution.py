"""
QUESTION:
Write a function called `find_the_index` that finds the index of the string "the" in a given encoded sentence. The sentence is encoded using a Caesar cipher with a shift value between 1 and 25. The function should return the index of "the" if found, or -1 otherwise. The function should only consider the lowercase and uppercase letters in the sentence.
"""

def find_the_index(sentence):
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
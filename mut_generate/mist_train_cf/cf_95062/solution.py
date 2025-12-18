"""
QUESTION:
Replace all occurrences of the word "a" with "the" in a given string while preserving the original word order and case. The function should be case-sensitive, i.e., "a" should be replaced with "the", "A" with "The", and "A" in all caps with "THE".
"""

def replace_a_with_the(text):
    words = text.split()  

    for i in range(len(words)):
        if words[i].lower() == "a":
            if words[i].islower():
                words[i] = "the"
            elif words[i].istitle():
                words[i] = "The"
            elif words[i].isupper():
                words[i] = "THE"

    return ' '.join(words)
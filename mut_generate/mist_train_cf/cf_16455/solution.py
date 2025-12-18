"""
QUESTION:
Create a function named `create_sentence` that takes a list of words as input and returns a sentence string. The list of words can contain special characters, numbers, and white spaces, but the function should only include words with alphanumeric characters (including words with internal spaces) in the output sentence. The output sentence should not have any leading or trailing white spaces.
"""

def create_sentence(words):
    sentence = ""
    for word in words:
        if word.replace(" ", "").isalnum():
            sentence += word + " "
    return sentence.strip()
"""
QUESTION:
Create a `syllables` function that takes in two parameters: a word and a tone. The function should return the meaning of the word based on its tone, handling homophones with the same pinyin but different meanings and tones in Mandarin Chinese. The function should return a message indicating that the homophone was not recognized with the given tone if the tone parameter does not match, and a message if the word is not recognized as a homophone.
"""

def syllables(word, tone):
    homophones = {'ma': {'mā': 'mother', 'má': 'numb', 'mǎ': 'horse', 'mà': 'scold'}}
    if word in homophones:
        if tone in homophones[word]:
            return homophones[word][tone]
        else:
            return "Homophone not recognized with the given tone."
    else:
        return "Word not recognized as a homophone."
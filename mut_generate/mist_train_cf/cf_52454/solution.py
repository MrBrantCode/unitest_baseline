"""
QUESTION:
Create a function named `headline_style` that takes a string of words as input and returns the string with the words rearranged according to the APA headline style. In this style, every word with three letters or more should be capitalized, and shorter words (except for the first and the last one) should be in lowercase. The function should work with any string of words, not just the provided example.
"""

def headline_style(headline):
    words = headline.split()  # Split the sentence into words
    for i in range(len(words)):
        # Words with 3 letters or more are capitalized, as well as the first and last word
        if len(words[i]) > 2 or i == 0 or i == len(words) - 1:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].lower()

    return ' '.join(words)  # join the list back into a string separated by spaces
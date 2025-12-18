"""
QUESTION:
Create a function called `title_case` that takes a string phrase as input and returns the phrase with the first letter of each word capitalized and all other letters in lowercase. The function should ignore non-alphabetic characters (such as numbers and special characters) and handle them as is. The function should also validate the input to ensure it is a string.
"""

def title_case(phrase):
    # validation
    if not isinstance(phrase, str):
        return "Invalid input! Please enter a string."

    # split the phrase into words
    words = phrase.split()

    # capitalize the first letter of each word and convert the rest to lowercase
    words = [word.capitalize() for word in words]

    # join the words back together
    phrase = ' '.join(words)

    return phrase
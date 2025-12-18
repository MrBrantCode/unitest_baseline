"""
QUESTION:
Write a function named `count_word_frequency` that takes a string as input. The function should normalize the string to lowercase, remove all punctuation marks (without using built-in functions or libraries to remove punctuation marks), and count the frequency of each word in the string. The function should also remove any stop words such as "and", "the", and "is" from the resulting dictionary (without using external resources or libraries to remove stop words). The function should return a dictionary with the word as the key and its frequency as the value.
"""

def count_word_frequency(text):
    """Counts the frequency of each word in the given text"""
    # Remove punctuation marks
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    translator = str.maketrans('', '', punctuation_marks)
    text = text.translate(translator)

    # Remove stop words
    stop_words = ["and", "the", "is"]
    words = text.lower().split()
    words = [word for word in words if word not in stop_words]

    # Count the frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
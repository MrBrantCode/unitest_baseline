"""
QUESTION:
Implement a function `count_word_frequency(text)` that takes a string `text` as input. The function should first convert the string to lowercase and remove all punctuation marks without using any built-in functions or libraries for this task. Then, it should split the string into words and count the frequency of each word, excluding the words "and", "the", and "is" (case-insensitive). The function should return a dictionary with each word as a key and its frequency as the value.
"""

def count_word_frequency(text):
    """Counts the frequency of each word in the given text"""
    # Manually define punctuation marks
    punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    
    # Remove punctuation marks from the given text
    text_without_punctuation = ""
    for char in text.lower():
        if char not in punctuation_marks:
            text_without_punctuation += char

    # Split the text into individual words
    words = text_without_punctuation.split()
    
    # Remove stop words from the list of words
    stop_words = ["and", "the", "is"]
    words = [word for word in words if word not in stop_words]
    
    # Count the frequency of each word
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency
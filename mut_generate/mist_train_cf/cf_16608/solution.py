"""
QUESTION:
Create a function called `create_frequency_chart` that takes a string `text` as input and returns a dictionary where the keys are unique words from the text and the values are the corresponding word frequencies. The function should have a time complexity of O(n), where n is the length of the text.
"""

def create_frequency_chart(text):
    frequency_chart = {}

    # Split the text into words
    words = text.split()

    # Iterate over each word in the text
    for word in words:
        # Check if the word is already in the frequency chart
        if word in frequency_chart:
            # Increment the frequency count by 1
            frequency_chart[word] += 1
        else:
            # Add the word to the frequency chart with a frequency count of 1
            frequency_chart[word] = 1

    return frequency_chart
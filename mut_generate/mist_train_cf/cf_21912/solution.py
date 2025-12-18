"""
QUESTION:
Write a function called `unique_words_in_alphabetical_order` that takes a string as input and returns a list of unique words in alphabetical order. The function should be case-insensitive, handle punctuation and special characters as word separators, and remove leading/trailing whitespace from each word. It should not use built-in sorting functions, data structures, regular expressions, or external libraries, and should have a time complexity of O(n^2) where n is the length of the input string.
"""

def unique_words_in_alphabetical_order(string):
    # Convert the string to lowercase
    string = string.lower()

    # Create a list to store the unique words
    unique_words = []

    # Iterate through each character in the string
    i = 0
    while i < len(string):
        # Find the start and end indices of each word
        if string[i].isalpha():
            start = i
            while i < len(string) and string[i].isalpha():
                i += 1
            end = i

            # Extract the word from the string
            word = string[start:end]

            # Remove any leading or trailing whitespace characters
            word = word.strip()

            # Check if the word is not already in the unique_words list
            if word not in unique_words:
                # Add the word to the unique_words list
                unique_words.append(word)

        i += 1

    # Sort the unique_words list in alphabetical order using bubble sort
    for i in range(len(unique_words)):
        for j in range(len(unique_words) - 1):
            if unique_words[j] > unique_words[j + 1]:
                unique_words[j], unique_words[j + 1] = unique_words[j + 1], unique_words[j]

    return unique_words
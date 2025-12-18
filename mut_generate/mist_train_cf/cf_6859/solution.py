"""
QUESTION:
Create a function named count_words that takes a comma-separated string as input and returns a dictionary where keys are words and values are their frequencies. The function should ignore any words containing the letter 'e' and only use a single loop to iterate over the string. It should not use built-in functions or libraries for string manipulation or dictionary operations, have a time complexity of O(n), and a space complexity of O(m), where n is the length of the input string and m is the number of unique words.
"""

def count_words(string):
    # Initialize an empty dictionary
    word_count = {}
    
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()
    
    # Initialize an empty string to store the current word
    current_word = ""
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is a letter or a comma
        if char.isalpha() or char == ',':
            # If it's a letter, add it to the current word
            if char.isalpha():
                current_word += char
        else:
            # If it's a non-alphabet character, it marks the end of a word
            # Ignore any word that contains the letter 'e'
            if 'e' not in current_word and current_word != "":
                # Add the word to the dictionary or increment its count if it already exists
                if current_word in word_count:
                    word_count[current_word] += 1
                else:
                    word_count[current_word] = 1
            
            # Reset the current word
            current_word = ""
    
    # Check if there's still a word left after the loop
    if 'e' not in current_word and current_word != "":
        if current_word in word_count:
            word_count[current_word] += 1
        else:
            word_count[current_word] = 1
    
    return word_count
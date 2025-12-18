"""
QUESTION:
Write a function named `count_sentences` that takes a string as input and returns the number of sentences in the string. The function should remove all punctuation marks except for periods, exclamation marks, and question marks, convert the string to lowercase, remove leading and trailing whitespaces, and remove any numbers. A sentence is defined as a sequence of words ending with a period, exclamation mark, or question mark. The function should be able to handle strings with multiple sentences and optimize for time complexity while maintaining readability without using built-in functions or libraries that directly solve the problem.
"""

def count_sentences(string):
    punctuation_marks = [".", "!", "?"]
    modified_string = ""
    
    for char in string:
        if char.isalpha() or char.isspace() or char in punctuation_marks:
            modified_string += char.lower()

    modified_string = modified_string.strip()
    
    words = modified_string.split()
    sentences = 0
    
    for word in words:
        if word[-1] in punctuation_marks:
            sentences += 1
    
    return sentences
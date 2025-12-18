"""
QUESTION:
Write a function `character_frequency_histogram` that takes a sentence as input and returns a table of character frequencies. The function should only consider alphabetical characters, ignore case sensitivity, and exclude characters with a frequency less than 2. The output table should be sorted in descending order of frequency and display each character and its frequency in separate columns.
"""

def character_frequency_histogram(sentence):
    """
    This function generates a table of character frequencies from a given sentence.
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    str: A table of character frequencies, excluding characters with a frequency less than 2, 
         sorted in descending order of frequency.
    """
    
    # Convert the sentence to lower case and filter out non-alphabetical characters
    filtered_sentence = ''.join(filter(str.isalpha, sentence.lower()))
    
    # Create a dictionary to store character frequencies
    frequency_dict = {}
    
    # Count the frequency of each character
    for char in filtered_sentence:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    # Filter out characters with a frequency less than 2 and sort the dictionary by frequency
    sorted_frequency_dict = dict(sorted({k: v for k, v in frequency_dict.items() if v >= 2}.items(), key=lambda item: item[1], reverse=True))
    
    # Generate the table
    table = "Character | Frequency\n--------- | ---------\n"
    for char, frequency in sorted_frequency_dict.items():
        table += f"{char}         | {frequency}\n"
    
    return table
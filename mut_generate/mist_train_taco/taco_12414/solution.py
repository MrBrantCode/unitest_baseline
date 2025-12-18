"""
QUESTION:
Internet search engines, such as Google, automatically sort and categorize web pages around the world to create a huge database. It also parses the search keywords entered by the user and creates an inquiry statement for database search.

In each case, complicated processing is performed to realize efficient search, but for the time being, all the basics are cutting out words from sentences.

So, please try to cut out the word from the sentence. This time, we will target English sentences with clear word breaks as follows.

* Target text: English text of 1024 characters or less, not including line breaks
* Delimiter: All are half-width characters, only spaces, periods, and commas.
* Words to cut out: Words with 3 to 6 letters (ignore words with 2 or less letters or 7 or more letters)



input

An English sentence consisting of delimiters and alphanumeric characters is given on one line (all half-width characters).

output

Please output the words separated by one space character (half-width) on one line.

Examples

Input

Rain, rain, go to Spain.


Output

Rain rain Spain


Input

Win today's preliminary contest and be qualified to visit University of Aizu.


Output

Win and visit Aizu
"""

def extract_valid_words(sentence: str) -> str:
    """
    Extracts words with 3 to 6 letters from the given English sentence.

    Parameters:
    - sentence (str): The input English sentence.

    Returns:
    - str: A string containing the valid words separated by a single space.
    """
    # Replace periods and commas with spaces
    cleaned_sentence = sentence.replace('.', ' ').replace(',', ' ')
    
    # Split the sentence into words
    words = cleaned_sentence.split()
    
    # Filter words with 3 to 6 letters
    valid_words = [word for word in words if 3 <= len(word) <= 6]
    
    # Join the valid words with a single space
    result = ' '.join(valid_words)
    
    return result
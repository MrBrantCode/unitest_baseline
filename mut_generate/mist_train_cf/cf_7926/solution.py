"""
QUESTION:
Write a function `find_common_words(str1, str2)` that takes two strings as input, and returns the number of common words between them. The function should only consider words that contain at least one uppercase letter. It should also print the unique common words in alphabetical order, excluding words that are less than three characters long or start with a vowel and end with a consonant. The time complexity of the function should be O(n + m), where n and m are the lengths of the input strings.
"""

def find_common_words(str1, str2):
    """
    This function finds the number of common words between two input strings, 
    considering only words with at least one uppercase letter. It also prints 
    unique common words in alphabetical order, excluding words less than three 
    characters long or those that start with a vowel and end with a consonant.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        int: The number of common words between the two input strings.
    """

    # Split the input strings into lists of words
    words1 = str1.split()
    words2 = str2.split()

    # Initialize an empty list to store common words
    common_words = []

    # Iterate over each word in the first list
    for word1 in words1:
        # Iterate over each word in the second list
        for word2 in words2:
            # Check if the words are equal and the first word starts with an uppercase letter
            if word1 == word2 and any(char.isupper() for char in word1):
                common_words.append(word1)

    # Remove duplicates from the list of common words
    common_words = list(set(common_words))

    # Sort the list of common words in alphabetical order
    common_words.sort()

    # Initialize an empty list to store unique common words that meet the conditions
    unique_common_words = []

    # Iterate over each common word
    for word in common_words:
        # Check if the word is at least three characters long and does not start with a vowel and end with a consonant
        if len(word) >= 3 and (word[0].lower() not in 'aeiou' or word[-1].lower() in 'aeiou'):
            unique_common_words.append(word)
            print(word)

    # Return the number of common words
    return len(common_words)
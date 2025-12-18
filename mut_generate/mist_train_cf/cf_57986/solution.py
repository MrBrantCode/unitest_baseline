"""
QUESTION:
Develop a function named find_max that takes a list of distinct words and an integer k as input. The function should return a tuple containing the word exhibiting the k-th highest quantity of individual characters, along with a dictionary containing the count of each unique character in that word. In cases where multiple strings possess the same count of unique characters, return the first one in the list. If k is greater than the number of distinct character counts, return None.
"""

def find_max(words, k):
    """
    This function takes a list of distinct words and an integer k as input.
    It returns a tuple containing the word exhibiting the k-th highest quantity of individual characters,
    along with a dictionary containing the count of each unique character in that word.
    
    If multiple strings possess the same count of unique characters, it returns the first one in the list.
    If k is greater than the number of distinct character counts, it returns None.
    """
    # Create a list to store tuples containing the word and its unique character count
    word_counts = []
    
    # Iterate over each word in the input list
    for word in words:
        # Create a set to store unique characters in the word
        unique_chars = set(word)
        
        # Create a dictionary to store the count of each unique character
        char_count = {char: word.count(char) for char in unique_chars}
        
        # Append a tuple containing the word and its unique character count to the list
        word_counts.append((word, len(unique_chars), char_count))
    
    # Sort the list in descending order based on the unique character count
    word_counts.sort(key=lambda x: x[1], reverse=True)
    
    # If k is greater than the number of distinct character counts, return None
    if k > len(word_counts):
        return None
    
    # Return the word exhibiting the k-th highest quantity of individual characters and its character count
    return (word_counts[k-1][0], word_counts[k-1][2])
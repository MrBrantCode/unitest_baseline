"""
QUESTION:
Write a function `compute_word_sums(words)` that takes an array of words as input and returns the array sorted in ascending order based on the sum of each word's characters converted to their corresponding numbers in the English alphabet (a=1, b=2, ..., z=26). The function should convert words to lowercase, ignore special characters and numbers, and have a time complexity of O(n log n), where n is the length of the array. The array will contain at most 100 words, each with at most 10 characters.
"""

def compute_word_sums(words):
    """
    Sorts an array of words based on the sum of each word's characters converted to their corresponding numbers in the English alphabet (a=1, b=2, ..., z=26).
    
    Args:
    words (list): A list of words.
    
    Returns:
    list: The sorted list of words.
    """
    
    def get_word_sum(word):
        """
        Computes the sum of a word's characters converted to their corresponding numbers in the English alphabet (a=1, b=2, ..., z=26).
        
        Args:
        word (str): A word.
        
        Returns:
        int: The computed sum.
        """
        word_sum = 0
        for char in word:
            if char.isalpha():
                word_sum += ord(char.lower()) - ord('a') + 1
        return word_sum
    
    return sorted([word.lower() for word in words], key=get_word_sum)
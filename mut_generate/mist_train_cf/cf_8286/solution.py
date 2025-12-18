"""
QUESTION:
Write a function `generate_ngrams` that takes in two parameters: 
- a string `sentence` consisting of words separated by spaces
- an integer `gram_size` representing the number of consecutive words in each n-gram

The function should return a list of all unique n-grams of size `gram_size` in the given `sentence`, in the order they appear. It should exclude punctuation marks from the words and handle sentences with words longer than 20 characters, consecutive punctuation marks, and multiple consecutive spaces. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(m), where m is the number of unique n-grams generated.
"""

def generate_ngrams(sentence, gram_size):
    """
    Generate all unique n-grams of size gram_size from a given sentence.

    Args:
    sentence (str): The input sentence.
    gram_size (int): The size of each n-gram.

    Returns:
    list: A list of unique n-grams in the order they appear.
    """
    # Split the sentence into words and remove punctuation marks
    words = [''.join(e for e in word if e.isalnum()).lower() for word in sentence.split()]
    
    # Initialize an empty list to store the generated n-grams
    ngrams = []
    
    # Iterate over the words in the sentence
    for i in range(len(words) - gram_size + 1):
        # Create the current n-gram
        ngram = ' '.join(words[i:i + gram_size])
        
        # Add the n-gram to the list if it is not already in the list
        if ngram not in ngrams:
            ngrams.append(ngram)
    
    # Return the list of unique n-grams
    return ngrams
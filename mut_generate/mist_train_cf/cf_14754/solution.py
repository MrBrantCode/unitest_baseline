"""
QUESTION:
Write a function named `wordCount` that takes a dataset of words as input and returns a list of tuples, where each tuple contains a word, its count, and its percentage of occurrence in the dataset. The output should be sorted in descending order of count. The input dataset is a collection of lines of text, and the output should be computed by splitting each line into words, counting the occurrence of each word, calculating the total number of words, and computing the percentage of occurrence for each word.
"""

def wordCount(dataset):
    """
    This function takes a dataset of words as input and returns a list of tuples, 
    where each tuple contains a word, its count, and its percentage of occurrence in the dataset.
    
    Args:
        dataset (list): A list of strings where each string is a line of text.
    
    Returns:
        list: A list of tuples containing word, count, and percentage of occurrence.
    """

    # Split each line into words
    words = [word for line in dataset for word in line.split()]
    
    # Count the occurrence of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Compute the total number of words in the dataset
    total_words = len(words)
    
    # Compute the percentage of occurrence for each word
    word_percentages = [(word, count, (count / total_words) * 100) for word, count in word_counts.items()]
    
    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_percentages, key=lambda x: x[1], reverse=True)
    
    return sorted_word_counts
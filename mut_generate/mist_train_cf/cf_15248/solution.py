"""
QUESTION:
Implement the `find_top_10_common_words` function to find the top 10 most common words in a given string while excluding common stop words. The function should take a string as input, convert it to lowercase, split it into words, exclude stop words, count the occurrences of each word, and return the top 10 most common words along with their counts. The solution should have a time complexity of O(n), where n is the length of the input string. The stop words should include at least "the", "and", "a", "is", etc.
"""

from collections import Counter

def find_top_10_common_words(string):
    stop_words = ["the", "and", "a", "is"]  # Add more stop words as needed

    words = string.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_words)
    top_10_words = word_counts.most_common(10)
    
    return top_10_words
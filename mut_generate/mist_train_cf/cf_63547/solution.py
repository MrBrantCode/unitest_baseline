"""
QUESTION:
Write a Python function named `map_reduce` that simulates the MapReduce process to count the total occurrences of each word in a given list of strings (representing books). The function should split the work into mapping word counts from each string and then reduce the results into a single dictionary. The function should return a dictionary where the keys are unique words and the values are their total counts.
"""

def map_reduce(books):
    """
    Simulates the MapReduce process to count the total occurrences of each word in a given list of strings (representing books).

    Args:
        books (list): A list of strings where each string represents a book.

    Returns:
        dict: A dictionary where the keys are unique words and the values are their total counts.
    """

    # Map: Split the work into mapping word counts from each string
    def map_word_counts(book):
        """Maps the word counts from a single book."""
        word_counts = {}
        for word in book.split():
            word = word.lower()  # Normalize the word to lowercase
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return word_counts

    # Map word counts from each book
    mapped_word_counts = [map_word_counts(book) for book in books]

    # Reduce: Combine the results into a single dictionary
    def reduce_word_counts(mapped_word_counts):
        """Combines the word counts from multiple books."""
        combined_word_counts = {}
        for word_counts in mapped_word_counts:
            for word, count in word_counts.items():
                if word in combined_word_counts:
                    combined_word_counts[word] += count
                else:
                    combined_word_counts[word] = count
        return combined_word_counts

    return reduce_word_counts(mapped_word_counts)
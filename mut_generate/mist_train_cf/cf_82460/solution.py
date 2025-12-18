"""
QUESTION:
Write a function `shortest_distance(dict, source, dest)` to find the shortest distance between two strings `source` and `dest` given a dictionary of words `dict`. The distance between two words can be defined in three different ways: 
1. The number of characters modified to transform one string into another with each step resulting in a valid word in `dict`.
2. The number of transitions between valid dictionary words, with each step being a valid direct transition.
3. The minimum single-character edits (insertions, deletions or substitutions) required to change one word into the other. 

Note that all words in `dict` have the same length.
"""

from collections import deque

def shortest_distance(dict, source, dest):
    """
    This function calculates the shortest distance between two strings `source` and `dest` 
    given a dictionary of words `dict`. The distance between two words is defined as 
    the minimum single-character edits (insertions, deletions or substitutions) required 
    to change one word into the other.

    Args:
        dict (list): A list of words with the same length.
        source (str): The source word.
        dest (str): The destination word.

    Returns:
        int: The shortest distance between `source` and `dest`.
    """

    # Create a set for O(1) look-up time
    dict_set = set(dict)

    # Initialize a queue for BFS, contains cells in the form (word, distance)
    queue = deque([(source, 0)])

    # Create a set to store visited words
    visited = set()

    while queue:
        word, distance = queue.popleft()

        # If the word is the destination, return the distance
        if word == dest:
            return distance

        # Mark the word as visited
        visited.add(word)

        # Generate all possible words by changing one character
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i + 1:]

                # If the generated word is in the dictionary and not visited, add it to the queue
                if next_word in dict_set and next_word not in visited:
                    queue.append((next_word, distance + 1))

    # If there is no path from source to dest, return -1
    return -1
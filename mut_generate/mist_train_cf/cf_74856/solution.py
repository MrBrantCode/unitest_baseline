"""
QUESTION:
Write a function `check_anagrams(cluster1, cluster2)` that takes two string inputs, `cluster1` and `cluster2`, and returns `True` if they are anagrams of each other (ignoring spaces and punctuation marks) and `False` otherwise.
"""

def check_anagrams(cluster1, cluster2):
    """Function to check whether given word clusters are anagrams"""
    from string import punctuation

    # Remove all punctuation marks using string.punctuation
    cluster1 = ''.join(char for char in cluster1 if char not in punctuation and char != ' ')
    cluster2 = ''.join(char for char in cluster2 if char not in punctuation and char != ' ')

    # Create sorted strings from the letters in the clusters
    sorted_cluster1, sorted_cluster2 = sorted(cluster1.lower()), sorted(cluster2.lower())

    # Check if sorted strings are the same - indicating an anagram
    return sorted_cluster1 == sorted_cluster2
"""
QUESTION:
Implement the `beam_search_with_pruning` function, which takes a list of tuples `vocab_probabilities` where each tuple contains a character and its corresponding probability, and a positive integer `cutoff_top_n` as inputs. The function should return a list of characters representing the top characters with the highest probabilities after pruning based on the `cutoff_top_n` number. Assume that `vocab_probabilities` is not empty and `cutoff_top_n` is less than or equal to the length of `vocab_probabilities`.
"""

def beam_search_with_pruning(vocab_probabilities, cutoff_top_n):
    # Sort the vocab_probabilities based on probabilities in descending order
    sorted_vocab = sorted(vocab_probabilities, key=lambda x: x[1], reverse=True)
    
    # Prune the sorted vocab based on cutoff_top_n
    pruned_vocab = sorted_vocab[:cutoff_top_n]
    
    # Extract the characters from the pruned_vocab
    top_characters = [char for char, _ in pruned_vocab]
    
    return top_characters
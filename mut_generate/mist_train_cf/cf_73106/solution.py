"""
QUESTION:
Create a function `search_substrings(text, subsets)` that performs a search operation for multiple character subsets within a provided text fragment. The function should implement a customized searching algorithm without using built-in substring search functions. It should return a dictionary where the keys are the subsets and the values are lists of indices at which each subset starts in the text fragment. The function should handle multiple occurrences of the same subset in the text.
"""

def search_substrings(text, subsets):
    subset_starts = {}

    # Iterate over each character subset
    for subset in subsets:
        subset_length = len(subset)
        
        # Iterate over the text fragment
        for i in range(len(text)):
            # Check if the current window matches the subset
            if text[i:i+subset_length] == subset:
                # Store the start index of the subset in the dictionary
                if subset not in subset_starts:
                    subset_starts[subset] = [i]
                else:
                    subset_starts[subset].append(i)

    return subset_starts
"""
QUESTION:
Implement the `info_gain` function, which calculates the information gain in a decision tree given two parameters: 
- `prev_dist`: A dictionary representing the distribution of classes in the parent node before the split, with class labels as keys and counts of items as values.
- `new_dist`: A list of dictionaries, each representing the distribution of classes in a child node after the split.

The function should use the formula: 
\[ \text{InfoGain} = \text{Entropy}(prev\_dist) - \sum_{i=1}^{n} \left( \frac{|S_i|}{|S|} \times \text{Entropy}(S_i) \right) \]
Where \( \text{Entropy}(dist) = - \sum_{i=1}^{n} p_i \times \log_2(p_i) \), \( |S| \) is the total number of items in the parent node, \( |S_i| \) is the number of items in the \( i^{th} \) child node, and \( p_i \) is the proportion of items in the \( i^{th} \) child node.

The function should also implement an `Entropy` function to calculate the entropy of a given distribution.
"""

import math

def info_gain(prev_dist, new_dist):
    def Entropy(dist):
        total_count = sum(dist.values())
        entropy = 0
        for count in dist.values():
            if count != 0:
                proportion = count / total_count
                entropy -= proportion * math.log2(proportion)
        return entropy

    prev_entropy = Entropy(prev_dist)
    total_items = sum(prev_dist.values())
    info_gain = prev_entropy
    for dist in new_dist:
        child_items = sum(dist.values())
        proportion = child_items / total_items
        info_gain -= proportion * Entropy(dist)
    return info_gain
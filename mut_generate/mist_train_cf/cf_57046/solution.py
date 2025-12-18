"""
QUESTION:
Create a function `pathInZigZagTree(label)` that returns the path from the root of a zigzag labelled binary tree to a node with a given `label`. The tree is structured such that every node has two children and the nodes are labelled in row order. The labelling is left to right in odd numbered rows and right to left in even numbered rows. The function should return the path as a list of node labels. Additionally, calculate the sum and product of all the labels in the path using a function `pathSumAndProduct(label)`. The `label` is an integer between 1 and 10^6.
"""

def pathInZigZagTree(label):
    result = []
    level = label.bit_length() - 1
    while label:
        result.append(label)
        level_end = 2 ** (level + 1) - 1
        level_start = 2 ** level
        label = (level_end + level_start - label) // 2
        level -= 1
    return result[::-1]

def pathSumAndProduct(label):
    path = pathInZigZagTree(label)
    path_sum = sum(path)
    path_product = 1
    for num in path:
        path_product *= num
    return path, path_sum, path_product
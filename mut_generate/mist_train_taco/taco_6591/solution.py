"""
QUESTION:
Indian summer is such a beautiful time of the year! A girl named Alyona is walking in the forest and picking a bouquet from fallen leaves. Alyona is very choosy — she doesn't take a leaf if it matches the color and the species of the tree of one of the leaves she already has. Find out how many leaves Alyona has picked.

Input

The first line contains an integer n (1 ≤ n ≤ 100) — the number of leaves Alyona has found. The next n lines contain the leaves' descriptions. Each leaf is characterized by the species of the tree it has fallen from and by the color. The species of the trees and colors are given in names, consisting of no more than 10 lowercase Latin letters. A name can not be an empty string. The species of a tree and the color are given in each line separated by a space.

Output

Output the single number — the number of Alyona's leaves.

Examples

Input

5
birch yellow
maple red
birch yellow
maple yellow
maple green


Output

4


Input

3
oak yellow
oak yellow
oak yellow


Output

1
"""

def count_unique_leaves(n, leaves):
    unique_leaves = {}
    count = 0
    
    for leaf in leaves:
        species, color = leaf.split()
        if species not in unique_leaves:
            unique_leaves[species] = set()
        if color not in unique_leaves[species]:
            unique_leaves[species].add(color)
            count += 1
    
    return count
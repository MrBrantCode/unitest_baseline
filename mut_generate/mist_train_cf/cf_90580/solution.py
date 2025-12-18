"""
QUESTION:
Write a function `find_unique_permutations(s)` that takes a string `s` as input and prints all its unique permutations in lexicographic order. The function should handle strings with duplicate characters and only print each unique permutation once. The output should be in lexicographic order.
"""

def find_unique_permutations(s):
    chars = sorted(list(s))
    unique_permutations = set()

    def permute(current, remaining):
        if len(current) == len(s):
            unique_permutations.add(''.join(current))
            return

        for i in range(len(remaining)):
            current.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            permute(current, new_remaining)
            current.pop()

    permute([], chars)
    sorted_permutations = sorted(list(unique_permutations))

    for permutation in sorted_permutations:
        print(permutation)
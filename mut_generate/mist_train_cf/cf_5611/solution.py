"""
QUESTION:
Write a function called `find_combinations` that generates all permutations of the input string, sorts them in descending order, and prints each permutation in reverse order. The function should have a time complexity of O(n^3 * n!), where n is the length of the string.
"""

def find_combinations(string):
    n = len(string)
    combinations = []

    def generate_combinations(string, current_combination, visited, length):
        if len(current_combination) == length:
            combinations.append(''.join(current_combination)[::-1])
            return

        for i in range(length):
            if not visited[i]:
                visited[i] = True
                current_combination.append(string[i])
                generate_combinations(string, current_combination, visited, length)
                visited[i] = False
                current_combination.pop()

    visited = [False] * n
    generate_combinations(string, [], visited, n)
    combinations.sort(reverse=True)

    for combination in reversed(combinations):
        print(combination)
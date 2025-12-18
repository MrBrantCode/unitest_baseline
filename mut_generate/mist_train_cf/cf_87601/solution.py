"""
QUESTION:
Write a function `find_subsets(s)` that prints all possible subsets of a given string `s` in lexicographical order. The function should not return any value, and the output should be printed to the console. The input string `s` may contain duplicate characters.
"""

def find_subsets(s):
    # Sort the string to ensure lexicographical order
    s = ''.join(sorted(s))

    # Recursive helper function to find subsets
    def find_subsets_helper(s, curr_subset, index):
        # Base case: when we reach the end of the string
        if index == len(s):
            # Print the current subset
            print(''.join(curr_subset))
            return

        # Exclude the current character and move to the next index
        find_subsets_helper(s, curr_subset, index + 1)

        # Include the current character and move to the next index
        find_subsets_helper(s, curr_subset + [s[index]], index + 1)

    # Start with an empty current subset and index 0
    find_subsets_helper(s, [], 0)
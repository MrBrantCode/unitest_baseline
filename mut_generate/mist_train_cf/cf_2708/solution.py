"""
QUESTION:
Write a function named `find_subsets` that takes a string `s` as input and prints all possible subsets of the string in lexicographical order. The function should not return any value (i.e., it should return `None`) and should only print the subsets.
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
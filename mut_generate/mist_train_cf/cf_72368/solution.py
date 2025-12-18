"""
QUESTION:
Create a function called `isAnagram` that takes two strings `string1` and `string2` as input and returns a boolean indicating whether the strings are anagrams of each other and the minimum number of swaps required to transform `string1` into `string2` if they are anagrams. The function should only consider lowercase English letters and the input strings should be between 1 and 10^5 characters in length.
"""

def isAnagram(string1, string2):
    """
    This function checks whether two strings are anagrams of each other and returns a boolean indicating the result.
    If they are anagrams, it also returns the minimum number of swaps required to transform string1 into string2.

    Parameters:
    string1 (str): The first input string.
    string2 (str): The second input string.

    Returns:
    tuple: A tuple containing a boolean indicating whether the strings are anagrams and the minimum number of swaps required.
    """

    # Check if the strings have the same length
    if len(string1) != len(string2):
        return False, -1

    # Create an array to count the characters
    count = [0] * 26

    # Count the characters in string1
    for char in string1:
        count[ord(char) - ord('a')] += 1

    # Count the characters in string2
    for char in string2:
        count[ord(char) - ord('a')] -= 1

    # Check if the character counts match
    for num in count:
        if num != 0:
            return False, -1

    # Initialize the number of swaps
    swaps = 0

    # Convert string1 to a list for swapping
    string1_list = list(string1)

    # Count the number of swaps required
    for i in range(len(string1)):
        while string1_list[i] != string2[i]:
            # Find the index of the character in string1_list
            j = string1_list.index(string2[i], i)
            # Swap the characters
            string1_list[i], string1_list[j] = string1_list[j], string1_list[i]
            # Increment the number of swaps
            swaps += 1

    return True, swaps
"""
QUESTION:
Write a function `check_permutation` that determines if two input strings are anagrams and calculates the number of permutations of the first string that are anagrams of the second string, without using in-built functions for string manipulation such as sorting or permutations. The function should return a tuple containing a message indicating whether the strings are anagrams and the number of permutations if they are, or 0 if they are not.
"""

def check_permutation(string1, string2):
    """
    This function determines if two input strings are anagrams and calculates 
    the number of permutations of the first string that are anagrams of the second string.

    Args:
        string1 (str): The first input string.
        string2 (str): The second input string.

    Returns:
        tuple: A tuple containing a message indicating whether the strings are anagrams 
        and the number of permutations if they are, or 0 if they are not.
    """

    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)

    def count_chars(s):
        count = [0] * 256
        for i in s:
            count[ord(i)] += 1
        return count

    if len(string1) != len(string2):
        return ("The strings are not anagrams of each other", 0)

    count1 = count_chars(string1)
    count2 = count_chars(string2)

    for i in range(256):
        if count1[i] != count2[i]:
            return ("The strings are not anagrams of each other", 0)

    duplicate_letters = [factorial(i) for i in count1 if i > 1]
    dup_product = 1
    for i in duplicate_letters:
        dup_product = dup_product * i

    total_permutations = factorial(len(string1)) // dup_product

    return ("The strings are anagrams of each other", total_permutations)
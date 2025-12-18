"""
QUESTION:
Design a function `longest_word(lexicon, letters)` that finds the longest word from the given `lexicon` list that can be formed using the characters in the `letters` list, considering character repetition. The function should return the longest word if found, and the solution should have optimal time complexity to handle scenarios with repeated characters in the `letters` list.
"""

def longest_word(lexicon, letters):
    counts = {}
    longest = ""

    # creating count map for given characters
    for char in letters:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for word in lexicon:
        temp_counts = counts.copy()  # create a copy of counts
        valid_word = True

        # For each word, iterate over each character in word
        for char in word:
            if char not in temp_counts or temp_counts[char] <= 0:
                valid_word = False
                break
            else:
                temp_counts[char] -= 1

        # If the word is valid and length of word is greater than longest found so far
        if valid_word and len(word) > len(longest):
            longest = word

    # returning longest word
    return longest
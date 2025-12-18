"""
QUESTION:
Write a function `most_frequent_letter` that finds the most frequent letter in a given sentence. The function should exclude any letters that appear more than once consecutively in the sentence. The input sentence will only contain English letters and spaces. If there are multiple letters with the same highest frequency, the function should return any one of them. If there are no letters that appear once in the sentence, the function should return an empty string or a message indicating that there are no letters that meet the condition.
"""

def most_frequent_letter(sentence):
    """
    Finds the most frequent letter in a given sentence excluding any letters that appear more than once consecutively.

    Args:
        sentence (str): The input sentence containing English letters and spaces.

    Returns:
        str: The most frequent letter in the sentence, or an empty string if no letters meet the condition.
    """
    sentence = sentence.replace(" ", "")
    max_count = 0
    max_letter = ''

    i = 0
    while i < len(sentence):
        count = 1
        j = i + 1
        while j < len(sentence) and sentence[i] == sentence[j]:
            count += 1
            j += 1

        if count == 1 and sentence[i] not in max_letter:
            if sentence.count(sentence[i]) > max_count:
                max_count = sentence.count(sentence[i])
                max_letter = sentence[i]
        i += count

    return max_letter
"""
QUESTION:
Given a list of phrases where each phrase is a string of lowercase English alphabets and spaces, generate a list of unique Before and After puzzles by combining two phrases such that the last word of the first phrase is the same as the first word of the second phrase. The sequence of the two phrases matters, and both sequences should be considered. The output should be a list of unique strings in lexicographical order.

The function should be named `beforeAndAfterPuzzles` and take a list of phrases as input. The length of the input list is between 1 and 100, and the length of each phrase is between 1 and 100.
"""

def beforeAndAfterPuzzles(phrases):
    end_dict = {}
    for phrase in phrases:
        end_word = phrase.split()[-1]
        if end_word not in end_dict:
            end_dict[end_word] = []
        end_dict[end_word].append(phrase)

    result_set = set()
    for phrase in phrases:
        first_word = phrase.split()[0]
        if first_word in end_dict:
            for old_phrase in end_dict[first_word]:
                if old_phrase != phrase:
                    result_set.add(old_phrase + phrase[len(first_word):])

    return sorted(list(result_set))
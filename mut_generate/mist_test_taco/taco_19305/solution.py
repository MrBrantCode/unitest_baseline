"""
QUESTION:
Given a standard english sentence passed in as a string, write a method that will return a sentence made up of the same words, but sorted by their first letter. However, the method of sorting has a twist to it:
* All words that begin with a lower case letter should be at the beginning of the sorted sentence, and sorted in ascending order.
* All words that begin with an upper case letter should come after that, and should be sorted in descending order.

If a word appears multiple times in the sentence, it should be returned multiple times in the sorted sentence. Any punctuation must be discarded.

## Example

For example, given the input string `"Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"`, your method should return `"and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut"`. Lower case letters are sorted `a -> l -> l -> o -> o -> t` and upper case letters are sorted `V -> T -> O -> M -> L -> C`.
"""

from string import punctuation

def sort_sentence_by_case(sentence: str) -> str:
    # Remove punctuation from the sentence
    t = str.maketrans('', '', punctuation)
    cleaned_sentence = sentence.translate(t)
    
    # Split the sentence into words
    words = cleaned_sentence.split()
    
    # Separate words into lower case and upper case
    lower_case_words = [word for word in words if word[0].islower()]
    upper_case_words = [word for word in words if word[0].isupper()]
    
    # Sort lower case words in ascending order
    sorted_lower_case_words = sorted(lower_case_words)
    
    # Sort upper case words in descending order
    sorted_upper_case_words = sorted(upper_case_words, reverse=True)
    
    # Combine the sorted words
    sorted_sentence = ' '.join(sorted_lower_case_words + sorted_upper_case_words)
    
    return sorted_sentence
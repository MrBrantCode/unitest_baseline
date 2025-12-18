"""
QUESTION:
Trigrams are a special case of the n-gram, where n is 3. One trigram is a continious sequence of 3 chars in phrase. [Wikipedia](https://en.wikipedia.org/wiki/Trigram)

 - return all trigrams for the given phrase 
 - replace spaces with \_ 
 - return an empty string for phrases shorter than 3

Example:

trigrams('the quick red') ==  the he\_ e\_q \_qu qui uic ick ck\_ k\_r \_re red
"""

def generate_trigrams(phrase: str) -> str:
    """
    Generate trigrams from the given phrase.

    Args:
        phrase (str): The input string from which trigrams are to be generated.

    Returns:
        str: A string containing all the trigrams separated by spaces. Returns an empty string if the phrase is shorter than 3 characters.
    """
    if len(phrase) < 3:
        return ""
    
    phrase = phrase.replace(' ', '_')
    trigrams = [phrase[i:i + 3] for i in range(len(phrase) - 2)]
    return ' '.join(trigrams)
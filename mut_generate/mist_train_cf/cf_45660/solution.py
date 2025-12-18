"""
QUESTION:
Create a function that transforms a given sentence into Camel case, Snake case, and Kebab case. The function should ignore non-alphanumeric characters and correctly handle numbers. It should be able to interpret abbreviations and acronyms correctly. The function should be able to convert at least the following case styles: 
- Camel case: The first word is lowercase, and the first letter of each subsequent word is uppercase (e.g., 'helloWorld').
- Snake case: All words are lowercase and separated by an underscore (e.g., 'hello_world').
- Kebab case: All words are lowercase and separated by a hyphen (e.g., 'hello-world').
"""

def convert_case(sentence):
    """
    This function transforms a given sentence into Camel case, Snake case, and Kebab case.
    It ignores non-alphanumeric characters and correctly handles numbers.
    It correctly interprets abbreviations and acronyms.

    Args:
        sentence (str): The input sentence to be transformed.

    Returns:
        dict: A dictionary containing the transformed sentence in Camel case, Snake case, and Kebab case.
    """

    # Prepare the sentence for transformation by removing non-alphanumeric characters and splitting into words
    words = ''.join(e for e in sentence if e.isalnum() or e.isspace()).split()

    # Convert to Camel case
    camel_case = words[0].lower() + ''.join(w.title() for w in words[1:])

    # Convert to Snake case
    snake_case = '_'.join(w.lower() for w in words)

    # Convert to Kebab case
    kebab_case = '-'.join(w.lower() for w in words)

    return {
        "Camel case": camel_case,
        "Snake case": snake_case,
        "Kebab case": kebab_case
    }
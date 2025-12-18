"""
QUESTION:
Create a function `count_example_and_break` that processes a list of words as follows: for each word, print 'success' if the word is "example", print 'failure' otherwise. If the word is "break", stop processing the list and print the number of words processed so far. After processing the list, print the total count of the word "example". The function should return the number of words processed.
"""

def count_example_and_break(list_of_words):
    """
    Process a list of words, printing 'success' for 'example', 'failure' otherwise.
    Stop processing when 'break' is encountered and print the number of words processed.
    Finally, print and return the total count of 'example'.

    Args:
        list_of_words (list): A list of words to be processed.

    Returns:
        int: The number of words processed.
    """
    count = 0

    for word in list_of_words:
        if word == "example":
            count += 1
            print("success")
        elif word == "break":
            print(f"Number of elements processed: {count}")
            break
        else:
            print("failure")

    print(f"Count of 'example': {count}")
    return count
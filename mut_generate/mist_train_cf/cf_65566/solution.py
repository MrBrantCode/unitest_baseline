"""
QUESTION:
Construct a function `palindrome_queue` that takes a queue of elements as input and returns the elements ordered in a palindrome sequence. The function should return the original queue if it is already a palindrome; otherwise, it should append the reversed queue to the original queue to create a palindrome sequence.
"""

def palindrome_queue(queue):
    """
    Construct a palindrome sequence from a given queue of elements.

    If the input queue is already a palindrome, return the original queue.
    Otherwise, append the reversed queue to the original queue to create a palindrome sequence.

    Args:
        queue (list): A list of elements.

    Returns:
        list: The elements ordered in a palindrome sequence.
    """

    reverse_queue = list(queue)[::-1]

    if queue == reverse_queue:
        return queue

    for item in reverse_queue:
        queue.append(item)

    return queue
"""
QUESTION:
Identify three patterns in a given sequence of numbers. The function name should be "find_patterns". The input is a list of integers. The function should return a list of three patterns as strings describing the identified patterns in the sequence.
"""

def find_patterns(sequence):
    """
    Identify three patterns in a given sequence of numbers.

    Args:
        sequence (list): A list of integers.

    Returns:
        list: A list of three patterns as strings describing the identified patterns in the sequence.
    """
    patterns = []

    # Check if the difference between each consecutive number increases by 1
    diff_sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    diff_diff_sequence = [diff_sequence[i + 1] - diff_sequence[i] for i in range(len(diff_sequence) - 1)]
    if all(diff == 1 for diff in diff_diff_sequence):
        patterns.append("The difference between each consecutive number increases by 1")

    # Check if the sum of each pair of consecutive numbers equals the next number in the sequence
    for i in range(len(sequence) - 2):
        if sequence[i] + sequence[i + 1] == sequence[i + 2]:
            patterns.append("The sum of each pair of consecutive numbers equals the next number in the sequence")
            break

    # Check if the sequence alternates between ascending and descending order
    is_ascending = sequence[0] < sequence[1]
    for i in range(1, len(sequence) - 1):
        if (sequence[i] < sequence[i + 1] and not is_ascending) or (sequence[i] > sequence[i + 1] and is_ascending):
            is_ascending = not is_ascending
        else:
            break
    else:
        patterns.append("The sequence alternates between ascending and descending order")

    return patterns
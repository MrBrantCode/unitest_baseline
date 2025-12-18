"""
QUESTION:
Write a function named `dyad_recurrence_rate` that takes two parameters: `text_string` and `dyad`. The function should calculate the recurrence rate of `dyad` within `text_string` by dividing the number of occurrences of `dyad` by the total possible occurrences. The function should return 0 if `dyad` is longer than `text_string` or if either `dyad` or `text_string` is empty.
"""

def dyad_recurrence_rate(text_string, dyad):
    dyad_count = 0
    text_length = len(text_string)
    
    # Check if the length of the dyad is larger than the text string
    # or if the dyad or the text string is empty
    if len(dyad) > text_length or not dyad or not text_string:
        return dyad_count

    # Traverse through the string and match the dyad
    for i in range(0, text_length - len(dyad) + 1):
        if text_string[i:i + len(dyad)] == dyad:
            dyad_count += 1

    # Calculate the recurrence rate
    recurrence_rate = dyad_count / (text_length - len(dyad) + 1)

    return recurrence_rate
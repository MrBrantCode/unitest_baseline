"""
QUESTION:
Create a recursive function `pattern(ch1, ch2, lines)` to print a custom pattern of alternating lines of two characters `ch1` and `ch2`. The pattern starts with a single occurrence of `ch1`, and each new line adds one additional occurrence of the respective character. The function should take no iterative loops and only use recursion. The function should print the pattern to the console, with the number of lines determined by the `lines` parameter.
"""

def entrace(ch1, ch2, lines, count=1):
    if lines == 0:
        return
    else:
        if count % 2 == 0:
            print(ch2 * count)
        else:
            print(ch1 * count)
        return entrace(ch1, ch2, lines-1, count+1)
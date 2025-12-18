"""
QUESTION:
Rng is going to a festival.

The name of the festival is given to you as a string S, which ends with `FESTIVAL`, from input. Answer the question: "Rng is going to a festival of what?" Output the answer.

Here, assume that the name of "a festival of s" is a string obtained by appending `FESTIVAL` to the end of s. For example, `CODEFESTIVAL` is a festival of `CODE`.

Constraints

* 9 \leq |S| \leq 50
* S consists of uppercase English letters.
* S ends with `FESTIVAL`.

Input

Input is given from Standard Input in the following format:


S


Output

Print the answer to the question: "Rng is going to a festival of what?"

Examples

Input

CODEFESTIVAL


Output

CODE


Input

CODEFESTIVALFESTIVAL


Output

CODEFESTIVAL


Input

YAKINIKUFESTIVAL


Output

YAKINIKU
"""

def extract_festival_name(S: str) -> str:
    """
    Extracts the name of the festival by removing the 'FESTIVAL' suffix from the input string.

    Parameters:
    S (str): The name of the festival, which ends with 'FESTIVAL'.

    Returns:
    str: The name of the festival without the 'FESTIVAL' suffix.
    """
    s_len = len(S)
    return S[:s_len - 8]
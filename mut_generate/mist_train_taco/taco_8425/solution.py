"""
QUESTION:
Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

* `S`  is misinterpreted as `5`
* `O` is misinterpreted as `0`
* `I` is misinterpreted as `1`

The test cases contain numbers only by mistake.
"""

def correct_digitised_text(text: str) -> str:
    """
    Corrects the errors in the digitised text by replacing misinterpreted characters.

    Parameters:
    text (str): The input string that may contain misinterpreted characters.

    Returns:
    str: The corrected version of the input string.
    """
    return text.translate(str.maketrans('501', 'SOI'))
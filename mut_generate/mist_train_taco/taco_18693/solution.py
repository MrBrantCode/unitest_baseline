"""
QUESTION:
Introduction 

Mr. Safety loves numeric locks and his Nokia 3310. He locked almost everything in his house. He is so smart and he doesn't need to remember the combinations. He has an algorithm to generate new passcodes on his Nokia cell phone. 


 Task 

Can you crack his numeric locks? Mr. Safety's treasures wait for you. Write an algorithm to open his numeric locks. Can you do it without his Nokia 3310? 

Input 

The `str` or `message` (Python) input string consists of lowercase and upercase characters. It's a real object that you want to unlock.

Output 
Return a string that only consists of digits.

Example
```
unlock("Nokia")  // => 66542
unlock("Valut")  // => 82588
unlock("toilet") // => 864538
```
"""

def unlock(message: str) -> str:
    """
    Converts a given message into a numeric passcode based on the mapping of letters to digits.

    Parameters:
    message (str): The input string consisting of lowercase and uppercase characters.

    Returns:
    str: A string of digits representing the numeric passcode.
    """
    return message.lower().translate(message.maketrans('abcdefghijklmnopqrstuvwxyz', '22233344455566677778889999'))
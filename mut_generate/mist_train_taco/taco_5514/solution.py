"""
QUESTION:
Student A and student B are giving each other test answers during a test.  
They don't want to be caught so they are sending each other coded messages.

Student A is sending student B the message: `Answer to Number 5 Part b`.  
He starts of with a square grid (in this example the grid = 5x5).  
He writes the message down (with spaces):

```
Answe
r to 
Numbe
r 5 P
art b
```

He then starts writing the message down one column at a time (from the top to the bottom).  
The new message is now: `ArNran u rstm5twob  e ePb`

You are the teacher of this class.  
Your job is to decipher this message and bust the students.

# Task

Write a function `decipher_message`.  
This function will take one parameter (`message`).  
This function will return the original message.  
*** Note: The length of the string is always going to be a prefect square ***

Hint: You should probably decipher the example message first before you start coding

Have fun !!!
"""

def decipher_message(message: str) -> str:
    """
    Deciphers a message that has been encoded by writing it in a square grid and reading it column by column.

    Parameters:
    message (str): The encoded message. The length of this string is always a perfect square.

    Returns:
    str: The original message before encoding.
    """
    n = int(len(message) ** 0.5)  # Calculate the size of the grid (n x n)
    return ''.join(message[i::n] for i in range(n))  # Reconstruct the original message
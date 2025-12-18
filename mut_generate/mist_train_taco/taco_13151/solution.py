"""
QUESTION:
A simple string contains a large repetition of letters within it. This problem is related to string handling and manipulation.  An original message is sent from planet Earth to planet Cybertron in form of a string. However, the letter position and string size is not important. The number of time each letter has occurred in the string is important. So the original string which is sent to Cybertron is encrypted in the new string which comprises the letters followed by each time it has occurred in the original string. Eg- original message is- abcdabf. Then the encrypted string is- a2b2c1d1f1

-----Input-----
The input consists of a single line string without any space or numeric or special characters.

-----Output-----
It will consist of in the encrypted string which comprises the letters followed by each time it has occurred in the original string in order.

-----Example-----
Input:
information

Output:
i2n2f1o2r1m1a1t1
"""

def encrypt_string(input_string: str) -> str:
    """
    Encrypts the input string by counting the occurrences of each character and 
    returning a new string with each character followed by its count.

    Parameters:
    input_string (str): The original string to be encrypted.

    Returns:
    str: The encrypted string.
    """
    if not input_string:
        return ""

    # Dictionary to store the count of each character
    char_count = {}
    
    # Count the occurrences of each character
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Build the encrypted string
    encrypted_string = ''.join(f"{char}{count}" for char, count in sorted(char_count.items()))
    
    return encrypted_string
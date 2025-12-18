"""
QUESTION:
The Hound and his brother the Mountain are engaged in a fight against each other in King's Landing. At the end of the fight, one dies and the other wins. They both are given a decimal number each in the 8 bit binary representation A and B. These numbers will decide their fate in the following manner:
If A^B ≤ B^A, then the Hound is declared as the winnner and the
    Mountain dies.

2.But if A^B >B^A, then the Mountain wins and the Hound dies.

Your task is to calculate and print the winner's name as output.

Input:: Input the number of testcases T in the first line. Followed by T lines, each line with input A and B.

Output: The name of the winner as "The Hound" or "The Mountain".

SAMPLE INPUT
7
00111011 01100101
00110011 11001100
01010101 10101010
01011100 10100111
11111100 01011000 
00101101 11001011
00101010 10101010

SAMPLE OUTPUT
The Mountain
The Mountain
The Mountain
The Mountain
The Hound
The Mountain
The Mountain
"""

def determine_winner(A: str, B: str) -> str:
    """
    Determines the winner between the Hound and the Mountain based on their 8-bit binary numbers.

    Args:
        A (str): An 8-bit binary string representing the Hound's number.
        B (str): An 8-bit binary string representing the Mountain's number.

    Returns:
        str: The name of the winner, either "The Hound" or "The Mountain".
    """
    a = int(A, 2)
    b = int(B, 2)
    
    if a ^ b <= b ^ a:
        return "The Hound"
    else:
        return "The Mountain"